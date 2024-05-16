import nltk
import requests
import spacy
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class classificationEntity:
    def response(self):
        response_list = []

        # 1. Tokenizar texto
        page = requests.get(
            "https://www.bbva.com/es/salud-financiera/que-son-rentas-recurrentes-y-como-afectan-a-la-salud-financiera/")
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text(strip=True)

        # Crear tokens por palabras
        tokens = word_tokenize(text, "Spanish")
        tokens = [word.lower() for word in tokens if word.isalpha()]

        # Verificar frecuencia de palabras
        freq = nltk.FreqDist(tokens)

        # Visualizar tokens
        freq.plot(30, cumulative=False)
        plt.close()

        # 2. Eliminar palabras de parada
        clean_tokens = [word for word in tokens if word not in stopwords.words('spanish')]

        # Verificar frecuencia de palabras
        freq_clean = nltk.FreqDist(clean_tokens)

        # Visualizar tokens
        freq_clean.plot(30, cumulative=False)
        plt.close()

        # 3a. Obtener sinónimos
        synonyms = [lemma.name() for syn in wordnet.synsets('investment') for lemma in syn.lemmas()]

        # Reemplazar tokens sinónimos
        clean_tokens_sin = [word.replace(syn, 'investment') for word in clean_tokens for syn in synonyms]

        # Recalcular frecuencia de palabras con sinónimos agregados
        freq_clean_sin = nltk.FreqDist(clean_tokens_sin)

        # Visualizar tokens
        freq_clean_sin.plot(30, cumulative=False)
        plt.close()

        # 3b. Obtener antónimos
        antonyms = [l.antonyms()[0].name() for syn in wordnet.synsets('good') for l in syn.lemmas() if l.antonyms()]

        # 4. Derivación Regresiva (Algoritmo de Porter)
        stemmer = PorterStemmer()

        # Regresión de derivación en textos en español
        spanish_stemmer = SnowballStemmer('spanish')

        clean_tokens_sin_stems = [spanish_stemmer.stem(token) for token in clean_tokens_sin]

        # Recalcular frecuencia de palabras con sinónimos agregados
        freq_clean_sin_stems = nltk.FreqDist(clean_tokens_sin_stems)

        # Visualizar Tokens
        freq_clean_sin_stems.plot(30, cumulative=False)
        plt.close()

        # 5. Palabras lematizadoras
        lemmatizer = WordNetLemmatizer()
        nlp = spacy.blank('es')

        # Lematizar tokens tras limpieza y convertidos en sinónimos
        clean_tokens_sin_lem = []

        for token in nlp(' '.join(clean_tokens_sin)):
            clean_tokens_sin_lem.append(token.text)

        freq_clean_sin_lem = nltk.FreqDist(clean_tokens_sin_lem)

        # Visualizar Tokens
        freq_clean_sin_lem.plot(30, cumulative=False)
        plt.close()

        return response_list
