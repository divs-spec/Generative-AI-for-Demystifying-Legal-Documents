from transformers import MarianMTModel, MarianTokenizer

TRANSLATORS = {}

SUPPORTED_LANGS = {
    "english": "en",
    "hindi": "hi",
    "chinese": "zh",
    "spanish": "es",
    "japanese": "ja"
}

# load translation model on demand
def get_translator(lang_code: str):
    if lang_code in TRANSLATORS:
        return TRANSLATORS[lang_code]
    model_name = f"Helsinki-NLP/opus-mt-en-{lang_code}" if lang_code != "en" else None
    if model_name:
        tok = MarianTokenizer.from_pretrained(model_name)
        mod = MarianMTModel.from_pretrained(model_name)
        TRANSLATORS[lang_code] = (tok, mod)
        return tok, mod
    return None

def translate_text(text: str, target_lang: str):
    if target_lang == "en":
        return text
    if target_lang not in SUPPORTED_LANGS.values():
        return text
    tok, mod = get_translator(target_lang)
    batch = tok([text], return_tensors="pt", padding=True)
    gen = mod.generate(**batch)
    return tok.decode(gen[0], skip_special_tokens=True)
