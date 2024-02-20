# Before running this script, install the Google Translate library:
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return {'original': text, 'translated': result.text}

# Take input for text to be translated
text_to_translate = input("Enter the text to be translated: ")
# Print the original text and translations for each language
print(f"\nOriginal Text: {text_to_translate}\n")

# Dictionary mapping full language names to language codes
language_options = {
    "Bengali": "bn",
    "Indonesian": "id",
    "Malay": "ms",
    "Myanmar": "my",
    "Nepali": "ne",
    "Tamil": "ta",
    "Chinese (Simplified)": "zh-CN"
}

# Iterate over target languages and perform translations
for language_name, language_code in language_options.items():
    try:
        translation = translate_text(text_to_translate, language_code)
        print(f"Translated Text to {language_name} ({language_code}): {translation['translated']}\n")
    except ValueError as e:
        print(f"Error translating to {language_name}: {e}")