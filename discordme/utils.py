import urllib.parse
import unicodedata

def encode_to_url_format(text):
    # Normaliser le texte pour séparer les modificateurs
    normalized_text = unicodedata.normalize("NFKD", text)
    # Encoder le texte normalisé
    cleaned_text = urllib.parse.quote(normalized_text)
    return cleaned_text