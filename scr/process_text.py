from nltk import tokenize
from nltk.corpus import stopwords
from string import punctuation
import unidecode
import re

class Process_Text():
    def __init__(self, contents:list) -> None:
        original_text = ' '.join([str(text) for text in contents])
        lower = self._lower_case(original_text)
        noise_removed = self._remove_noises(lower)
        without_accents = self._remove_accents(noise_removed)
        tokenized = self._tokenize(without_accents)
        withou_stop_words = self._stop_words(tokenized)
        return withou_stop_words

    def _lower_case(self, text:str):
        '''
        '''

        return text.lower()

    def _remove_noises(self, text):
        '''
        '''

        regex = '\n'
        text = re.sub(regex, '', text)
        regex = '[\d\(\)\%,;.?!"\'—/]'
        text = re.sub(regex, '', text)
        text = ' '.join(text.split())

        return text
    
    def _remove_accents(self, text):
        '''
        '''

        return unidecode.unidecode(text)

    def _tokenize(self, text):
        '''
        '''

        return tokenize.word_tokenize(text, language='portuguese')

    def _stop_words(self, words):
        '''
        '''

        stop_words = set(stopwords.words('portuguese') + list(punctuation))
        words_withous_sw = [word for word in words if word not in stop_words]

        return words_withous_sw