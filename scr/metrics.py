from itertools import chain
from collections import Counter


def _return_counter(a_lists):
    '''
    '''
    
    counterize = []
    for a_list in a_lists:
        count = Counter(a_list)
        counterize.append(count)
    return counterize

def _return_unique_words(a_lists):
    '''
    '''

    words = sorted(set(list(chain(*a_lists))))
    a_word = {}
    for word in words:
        a_word[word] = {'tf':[], 'df':0, 'idf':0, 'tfidf':[]}
    return a_word

def _get_tf():
    pass

def _get_idf():
    pass

def _get_tfidf():
    pass

def _fill_table(a_lists):
    word_count_per_doc = _return_counter(a_lists)
    table_with_metrics = _return_unique_words(a_lists)

    for key, value in table_with_metrics.items():
        tf = _get_tf()
        idf = _get_idf()
        tfidf = _get_tfidf()
    
    return 1


def get_metrics_of_text(a_lists):
    '''
    '''

    words_table_metrics = _fill_table(a_lists)