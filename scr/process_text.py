from nltk import tokenize
from nltk.corpus import stopwords
from string import punctuation
import unidecode
import re

class Process_Text():
    def __init__(self, contents:list):
        '''
        Classe responsável pelo pré-processamento do texto.

        Parameter:
            contents (list) Uma lista com o conteúdo dos documentos.
        '''

        original_text = ' '.join([str(text) for text in contents])
        lower = self._lower_case(original_text)
        noise_removed = self._remove_noises(lower)
        without_accents = self._remove_accents(noise_removed)
        tokenized = self._tokenize(without_accents)
        without_stop_words = self._stop_words(tokenized)
        
        self.all_contents = without_stop_words

    def _lower_case(self, text:str):
        '''
        Transforma o texto para lower case.
        '''

        return text.lower()

    def _remove_noises(self, text):
        '''
        Remove os ruídos (caracteres de pontuações, duplo espaços, etc).
        '''

        regex = '\n'
        text = re.sub(regex, '', text)
        regex = '[\d\(\)\%,;.?!"\'—/]'
        text = re.sub(regex, '', text)
        text = ' '.join(text.split())

        return text
    
    def _remove_accents(self, text):
        '''
        Remove os acentos das palavras.
        '''

        return unidecode.unidecode(text)

    def _tokenize(self, text):
        '''
        Tokeniza o texto.
        '''

        return tokenize.word_tokenize(text, language='portuguese')

    def _stop_words(self, words):
        '''
        Remove as palavras consideradas como Stop Words.
        '''
        custom = ['i', 'se', 'ate', 'nao', 'tal']

        stop_words = set(stopwords.words('portuguese') + \
            list(punctuation) + custom)
        words_withous_sw = [word for word in words if word not in stop_words]

        return words_withous_sw