import stanza


class Lemmatizer():
    def __init__(self,list_texts_tokenized):
        self.list_texts_tokenized = list_texts_tokenized
    
    def lemmatizer_text(self,text_tokenized):
        nlp = stanza.Pipeline(lang='en', processors='tokenize,lemma', lemma_pretagged=True,tokenize_pretokenized=True )
        doc = nlp([text_tokenized])
        text_lemma = [word.lemma for sentence in doc.sentences for word in sentence.words]
        return text_lemma
    
    def concat_list_text(self,list_for_concat):
        join_all_texts = list_for_concat[0]
        for texts in list_for_concat[1:]:
            join_all_texts = join_all_texts + texts
        
        return join_all_texts
    
    def lemmatizer_all_texts(self):
        if type(self.list_texts_tokenized[0]) == str:
           return self.lemmatizer_text(self.list_texts_tokenized)
        else:
           lemmatized_texts = []
           for tokens in self.list_texts_tokenized:
              lemmatized_texts.append(self.lemmatizer_text(tokens))
           return lemmatized_texts

    def get_all_texts_lemmatized(self):
          if type(self.list_texts_tokenized[0]) == str:
              return self.lemmatizer_text(self.list_texts_tokenized)
          else:
              list_for_concat = self.lemmatizer_all_texts()
              return self.concat_list_text(list_for_concat)

    
            

    
