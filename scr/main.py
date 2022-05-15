import preprocess_file
import stannize
import metrics
from print_word_cloud import PrintWordCloud

my_list = preprocess_file.get_preprocessed_files()

# my_list = [
#     ['comeu','gato','queijo'],
#     ['gato', 'gato'],
#     ['gato']
# ]

doc = stannize.get_words_stannizeds(my_list)



topn_words_table, words_proximities = \
    metrics.get_metrics_of_text(my_list)

qtd_pontos_centrais = int =  3
PrintWordCloud(topn_words_table, words_proximities, qtd_pontos_centrais)