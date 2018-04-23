# job: understands how to prepare raw text for further analysis
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords  
from gensim import parsing
import gensim
import re

class preprocessor():
    def __init__(self):
        return None

    def transformText(self, text):
        """
        input
            text(str): text to be processed
            word_size(int): the minimum length of words that will be kept in the output.
            stopword_lang(str): lowercase language name used for choosing stopwords 

        output
            (str): a string of extracted words seperated with a single whitespace.
        """
        text = gensim.corpora.textcorpus.strip_multiple_whitespaces(text)
        text = text.strip()
        text = text.lower()
        
        return text