from translate import Translator

def translate_data(input_text, target_language):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(input_text)
    return translated_text

# Get input text from the user
input_text = input("Enter the text you want to translate: ")

# Language options
languages = {
    '1': {'code': 'en', 'name': 'English'},
    '2': {'code': 'es', 'name': 'Spanish'},
    '3': {'code': 'fr', 'name': 'French'},
    '4': {'code': 'hi', 'name': 'Hindi'},
    '5': {'code': 'de', 'name': 'German'}
}

# Display language options
print("Select the target language:")
for code, language in languages.items():
    print(f"{code}: {language['name']}")

# Get target language choice from the user
target_language = input("Enter the number corresponding to the target language: ")

# Translate the input text
if target_language in languages:
    translated_text = translate_data(input_text, languages[target_language]['code'])
    print("Translated text:")
    print(translated_text)
else:
    print("Invalid language selection. Translation cannot be performed.")
