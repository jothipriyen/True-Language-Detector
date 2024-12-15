from langdetect import detect, detect_langs


def detect_language(text):
    try:
        # Detect the language and probabilities
        language = detect(text)
        probabilities = detect_langs(text)
        
        # Extract language probabilities in a readable format
        probabilities_str = ", ".join([f"{lang.lang}: {lang.prob}" for lang in probabilities])
        
        return language, probabilities_str
    except Exception as e:
        return str(e)  # Return the error message if something goes wrong


if _name_ == "_main_":
    user_input = input("Enter text to detect language: ")
    lang, details = detect_language(user_input)
    print(f"Detected Language: {lang}")
    print(f"Language Probabilities: {details}")