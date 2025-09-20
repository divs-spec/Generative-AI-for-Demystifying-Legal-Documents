import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from src.data_processing import extract_text_from_pdf, simple_clause_split, chunk_text
from src.model import LegalSimplifier
from src.infer import DocQA
from src.utils import translate_text, SUPPORTED_LANGS

UPLOAD_FOLDER = 'data/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'replace-with-a-secure-secret'

simplifier = LegalSimplifier(model_name='t5-small')
qa = DocQA(simplifier)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', languages=SUPPORTED_LANGS.keys())

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    file = request.files['file']
    level = request.form.get('level', 'medium')
    language = request.form.get('language', 'english')
    lang_code = SUPPORTED_LANGS.get(language.lower(), 'en')

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        # extract text
        if filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(path)
        else:
            text = open(path, 'r', encoding='utf-8').read()

        clauses = simple_clause_split(text)
        simplified = []
        for c in clauses[:30]:
            sim = simplifier.simplify(c, level=level, max_length=200)
            sim = translate_text(sim, lang_code)
            simplified.append(sim)

        chunks = chunk_text(text)
        qa.build_vector_store(chunks)

        return render_template('result.html', clauses=zip(clauses, simplified), lang=language, level=level)
    flash('File type not allowed')
    return redirect(url_for('index'))

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    language = request.form.get('language', 'english')
    lang_code = SUPPORTED_LANGS.get(language.lower(), 'en')
    if not question:
        return {"error": "no question provided"}, 400
    ans, hits = qa.query(question)
    ans = translate_text(ans, lang_code)
    return {"answer": ans, "sources": hits}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
