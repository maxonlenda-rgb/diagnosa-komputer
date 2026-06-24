import json

def load_gejala():
    with open("data/gejala.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_diagnosa():
    with open("data/diagnosa.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_rules():
    with open("data/rules.json", "r", encoding="utf-8") as f:
        return json.load(f)