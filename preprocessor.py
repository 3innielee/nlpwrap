# job: understands how to prepare raw text for further analysis
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer 
from gensim import parsing
import gensim
import re

class preprocessor():
    def __init__(self):
        return None

    def getTransformedString(self, text, word_size=3, stopword_lang="english"):
        filtered_list=self._transformText(text, word_size, stopword_lang)
        return " ".join(filtered_list)

    def getTransformedList(self, text, word_size=3, stopword_lang="english"):
        return self._transformText(text, word_size, stopword_lang)

    def _transformText(self, text, word_size, stopword_lang):
        """
        input
            text(str): text to be processed
            word_size(int): the minimum length of words that will be kept in the output.
            stopword_lang(str): lowercase language name used for choosing stopwords 

        output
            (list): a list of extracted words.
        """
        text = gensim.corpora.textcorpus.strip_multiple_whitespaces(text)
        text = text.strip()
        text = text.lower()
        text = gensim.parsing.preprocessing.strip_numeric(text)

        text = gensim.parsing.preprocessing.strip_punctuation(text)

        lemm = WordNetLemmatizer()
        stops = set(stopwords.words(stopword_lang))
        filtered_words=[lemm.lemmatize(word) for word in text.split() if word not in stops]

        filtered_words = gensim.corpora.textcorpus.remove_short(filtered_words, minsize=word_size)     
        
        return filtered_words