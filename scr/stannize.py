import stanza

def get_words_stannizeds(inner_lists):
    '''
    '''
    nlp = stanza.Pipeline(lang='pt', processors='tokenize, lemma')
    stanzed_list = []
    for a_list in inner_lists:
        joined_words = " ".join([' '.join(a_list)])
        doc = nlp(joined_words)

        stanzed_list.append([
            {'id':word.id, 
             'word':word.text,
             'lemma':word.lemma} \
                 for sent in doc.sentences \
                    for word in sent.words])


    return stanzed_list
    