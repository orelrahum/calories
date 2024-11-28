import os
import json
from googletrans import Translator

def translate_names(folder_path, target_language='he'):
    translator = Translator()
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for item in data:
                if 'name' in item:
                    translated = translator.translate(item['name'], dest=target_language)
                    item['name'] = translated.text
            
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

# Example usage
folder_path = '..\\src\\foods\\builtIn'
translate_names(folder_path)