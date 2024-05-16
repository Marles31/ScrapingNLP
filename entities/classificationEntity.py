import nltk
import requests
import spacy
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import seaborn as sns
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


class classificationEntity:

    def response(self):

        # 1. Tokenizar texto
        response_list = []

        page = requests.get(
            "https://www.bbva.com/es/salud-financiera/que-son-rentas-recurrentes-y-como-afectan-a-la-salud-financiera/")
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text(strip=True)
        print(text)

        # Crear tokens por palabras
        tokens = word_tokenize(text, "Spanish")
        tokens = [word.lower() for word in tokens if word.isalpha()]
        # Remover los signos de puntuación
        print(tokens)

        # Verficar frecuencia de palabras
        freq = nltk.FreqDist(tokens)
        for key, val in freq.items():
            print(str(key) + ':' + str(val))

        # Visualizar tokens
        sns.set()
        freq.plot(30, cummulative=False)

        # 2. Eliminar palabras de parada
        clean_tokens = tokens[:]
        for token in tokens:
            if token in stopwords.words('spanish'):
                clean_tokens.remove(token)
        print(clean_tokens)

        # Verificar frecuencia de palabras
        freq_clean = nltk.FreqDist(clean_tokens)
        for key, val in freq_clean.items():
            print(str(key) + ':' + str(val))

        # Visualizar tokens
        sns.set()
        freq_clean.plot(30, cumulative=False)

        # 3. Obtener sinónimos
        synonyms = []
        for syn in wordnet.synsets('investment'):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        print(synonyms)

        # Reemplazar tokens sinónimos
        for ind, sin in enumerate(synonyms):
            clean_tokens_sin = [word.replace(synonyms[ind], 'investment')
                                for word in clean_tokens]

        # Reemplazar tokens sinóimos manual
        sinonimos = ['libertad', 'independencia']

        # Synonyms and Antonyms
        antonyms = []
        for syn in wordnet.synsets('good'):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        print(antonyms)

        # 4. Porter Algorithm Regressive derivation
        stemmer = PorterStemmer()
        print(stemmer.stem('eating'))

        # Regressive derivation in spanish texts
        spanish_stemmer = SnowballStemmer('spanish')
        print(spanish_stemmer.stem('trabajando'))
        print(spanish_stemmer.stem('trabajo'))

        clean_tokens_sin_stems = [spanish_stemmer.stem(token) for token in clean_tokens_sin]
        print(clean_tokens_sin_stems)

        # Frequency word recalculation with added synonyms
        freq_clean_sin_stems = nltk.FreqDist(clean_tokens_sin_stems)
        for key, val in freq_clean_sin_stems.items():
            print(str(key) + ':' + str(val))
        # Visualise Tokens
        freq_clean_sin_stems.plot(30, cumulative=False)

        # 5. Legitimatizing words
        lemmatizer = WordNetLemmatizer()
        print(lemmatizer.lemmatize('working', pos="v"))
        nlp = spacy.blank('es')

        # response_info = {
        #     "text": text,
        #     "tokens": tokens,
        #     "frequency": freq.items(),
        #     "clean_tokens": clean_tokens
        # }

        # response_list.append(response_info)

        return response_list
