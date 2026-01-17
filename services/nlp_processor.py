import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("portuguese"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"[^a-záàâãéèêíïóôõöúçñ\s]", " ", text)

    words = text.split()

    processed_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(processed_words)

print("NLTK funcionando")
