from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Trainer, TrainingArguments
import torch


# Example fine-tuning script for summarization


def fine_tune(model_name: str = "t5-small", output_dir: str = "./finetuned-model"):
dataset = load_dataset("json", data_files={"train": "data/annotations.jsonl"})


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def preprocess(batch):
inputs = batch["text"]
targets = batch["summary"]
model_inputs = tokenizer(inputs, max_length=512, truncation=True)
labels = tokenizer(targets, max_length=128, truncation=True)
model_inputs["labels"] = labels["input_ids"]
return model_inputs


tokenized = dataset["train"].map(preprocess, batched=True)


collator = DataCollatorForSeq2Seq(tokenizer, model=model)


training_args = TrainingArguments(
output_dir=output_dir,
evaluation_strategy="no",
learning_rate=5e-5,
per_device_train_batch_size=4,
num_train_epochs=1,
weight_decay=0.01,
save_total_limit=2,
logging_steps=10,
)


trainer = Trainer(
model=model,
args=training_args,
train_dataset=tokenized,
data_collator=collator,
tokenizer=tokenizer,
)


trainer.train()
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)


if __name__ == "__main__":
fine_tune()
