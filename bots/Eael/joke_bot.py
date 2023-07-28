import json

def load_jokes(file_path: str) -> dict:
  with open(file_path, 'r') as file:
    data: dict = json.load(file)
  return data

def save_jokes(file_path: str, data: dict):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)
