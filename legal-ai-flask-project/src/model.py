from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

class LegalSimplifier:
    def __init__(self, model_name: str = 't5-small', device: int = None):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        if device is None:
            self.device = 0 if torch.cuda.is_available() else -1
        else:
            self.device = device
        self.pipe = pipeline('text2text-generation', model=self.model, tokenizer=self.tokenizer, device=self.device)

    def simplify(self, text: str, level: str = "medium", max_length: int = 256) -> str:
        level_map = {
            "very_basic": "Explain in very simple terms like for a 10-year-old: ",
            "medium": "Simplify clearly: ",
            "intermediate": "Provide moderately detailed explanation: ",
            "advanced": "Explain in detail with technical clarity: "
        }
        prefix = level_map.get(level, "Simplify: ")
        if 't5' in self.model_name:
            prompt = "simplify: " + prefix + text
        else:
            prompt = prefix + text
        out = self.pipe(prompt, max_length=max_length, truncation=True)
        return out[0]['generated_text']
