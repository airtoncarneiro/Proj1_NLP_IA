import preprocess_file
import stannize
import metrics

#lista = preprocess_file.get_preprocessed_files()
#print(lista)

lista = [
    ['comeu','gato','queijo'],
    ['gato', 'gato'],
    ['gato']
]

# doc = stannize.get_words_stannizeds(lista)

# print(doc)


topn_tfidf = metrics.get_metrics_of_text(lista)