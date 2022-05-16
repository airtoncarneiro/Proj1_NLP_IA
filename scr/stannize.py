import stanza

def get_words_stannizeds(inner_lists:list)->list:
    '''
    Faz o processo de tokenização e lemmatização do texto.
    Parameter: (list) Uma lista de palavras de cada documento.
    Return: (list) Retorna a lista de palavras lematizadas por documento.
    '''
    nlp = stanza.Pipeline(lang='pt', processors='tokenize,lemma')
    docs_in_lemman = []
    for a_list in inner_lists:
        joined_words = " ".join([' '.join(a_list)])
        doc = nlp(joined_words)
        
        docs_in_lemman.append([
            word.lemma \
                 for sent in doc.sentences \
                    for word in sent.words])


    return docs_in_lemman
    