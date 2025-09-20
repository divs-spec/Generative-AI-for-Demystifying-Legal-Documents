# Generative-AI-for-Demystifying-Legal-Documents
Python + Flask Project


# Legal Document Simplifier

This project uses **Generative AI** (transformers) with a **Flask** web app to simplify legal documents into plain, accessible language. Users can upload legal documents, choose explanation complexity (Very Basic → Advanced), select their preferred language (English, Hindi, Chinese, Spanish, Japanese, etc.), and ask interactive Q\&A questions about the document.

⚠️ **Disclaimer:** This tool is intended for educational and informational purposes only. It is **not a substitute for professional legal advice**.

---

## Features

✅ Simplify legal documents into plain language

✅ Multiple explanation levels: Very Basic → Advanced

✅ Multi-language support (English, Hindi, Chinese, Spanish, Japanese, etc.)

✅ Upload documents (PDF, TXT)

✅ Interactive Question-Answering (ask about uploaded document)

✅ Fine-tuning option with `annotations.jsonl` dataset

✅ Frontend built with HTML, CSS, and JavaScript

✅ Backend powered by Flask + Hugging Face Transformers

---

## Core Features

🔹 Natural Language Simplification

🔹 Hierarchical Abstraction Levels

🔹 Multilingual Rendering

🔹 Document Embedding + Vector Search

🔹 Domain-Specific Fine-Tuning

🔹 End-to-End Pipeline — Covers preprocessing (PDF → text), simplification, translation, storage, and retrieval in one unified framework.

---

## Societal Benefits

✅ Legal Accessibility — Empowers average citizens to interpret rental agreements, loan contracts, and terms of service without requiring specialized legal literacy.

✅ Consumer Protection — Highlights obligations, risks, and penalty clauses that are often obscured in dense contractual text.

✅ Linguistic Inclusivity — Bridges the gap for non-English speakers by providing localized explanations in their native language.

✅ Educational Utility — Assists students, paralegals, and small business owners in learning contractual norms and legal reasoning.

✅ Democratization of Legal Knowledge — Reduces dependency on costly legal intermediaries for basic interpretative tasks.

---

## Project Structure

```
legal-ai-flask-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── sample_legal_docs/
│   │   ├── rental_agreement.txt
│   │   ├── loan_contract.txt
│   │   └── terms_of_service.txt
│   ├── annotations.jsonl
│   └── uploads/
│       └── .gitkeep
├── src/
│   ├── data_processing.py
│   ├── model.py
│   ├── train.py
│   ├── infer.py
│   └── utils.py
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── styles.css
```

---

## Requirements

### Python version

* Python **3.9+** recommended

### Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
flask==2.2.5
transformers==4.50.0
datasets==2.10.1
torch>=1.13.0
faiss-cpu==1.7.4
sentence-transformers==2.2.2
pdfplumber==0.7.6
python-multipart==0.0.5
gunicorn==20.1.0
```

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/legal-ai-flask-project.git
cd legal-ai-flask-project
```

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install requirements**

```bash
pip install -r requirements.txt
```

4. **Ensure folder structure is correct**

```bash
mkdir -p data/uploads
# Keep folder tracked by Git
touch data/uploads/.gitkeep
```

---

## Running the Application

### Development mode

```bash
python app.py
```

Then open: [http://localhost:5000](http://localhost:5000)

### Production mode (Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Usage

1. Navigate to the web app home page.
2. Upload a legal document (PDF/TXT).
3. Choose explanation level:

   * Very Basic (child-friendly)
   * Medium (simple, clear)
   * Intermediate (moderately detailed)
   * Advanced (technical clarity)
4. Choose output language.
5. View simplified explanations clause by clause.
6. Ask questions about the document using the built-in Q\&A.

---

## Sample Data

* `data/sample_legal_docs/` contains example contracts.
* `data/annotations.jsonl` provides fine-tuning data with text-summary pairs.

Example from `annotations.jsonl`:

```json
{"text": "The tenant agrees to pay monthly rent of $1,200 by the 5th of each month.", "summary": "You must pay $1,200 rent by the 5th of each month."}
```

---

## Fine-tuning (Optional)

To fine-tune on your dataset:

```bash
python src/train.py
```

This will train a summarization model on `data/annotations.jsonl` and save it under `./finetuned-model/`.

---

## Git Setup for Uploads

To avoid committing user-uploaded documents, `.gitignore` includes:

```gitignore
# Ignore uploaded user files
data/uploads/*
# Keep empty folder
!data/uploads/.gitkeep
```

---

## Demo Script (Step-by-Step)

1. Start the Flask server:

```bash
python app.py
```

2. Open browser at [http://localhost:5000](http://localhost:5000).
3. Upload a sample file from `data/sample_legal_docs/`.
4. Choose explanation level (e.g., Very Basic).
5. Choose language (e.g., Hindi).
6. View simplified results.
7. Ask: *“What happens if I don’t pay on time?”* in the Q\&A box.

---

## Notes

* Some translations rely on Hugging Face MarianMT; not all languages may be equally strong.
* Long documents may be chunked; very large contracts may take longer.
* For production, deploy with Gunicorn + Nginx (or Cloud Run).

---

## Future Extensions

⚙️ Clause Risk Classification — Highlight unfair terms and risky obligations.

🔍 Regulatory Compliance Checker — Map clauses against jurisdictional compliance benchmarks.

📊 Explainability Layer — Provide attention-visualization for model interpretability.

☁️ Cloud-Native Deployment — Containerization via Docker + deployment on Google Cloud Run or Kubernetes.

---

## Conclusion

This project operationalizes AI-driven legal simplification with a focus on human accessibility, linguistic equity, and social empowerment. By bridging the gap between legal complexity and public comprehension, it enhances transparency, reduces exploitation risks, and contributes to a more informed civil society.

---

## License

MIT License. Free to use and adapt with attribution.

---

🎉 This project is now **fully presentation-ready** with a clear workflow, commands, and guidelines.
