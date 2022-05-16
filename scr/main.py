import preprocess_file
import stannize
import metrics
from print_word_cloud import PrintWordCloud

my_list = preprocess_file.get_preprocessed_files()

doc = stannize.get_words_stannizeds(my_list)

# informa a quantidade de pontos centrais
# que também será o top n palavras
qtd_pontos_centrais = int =  5
topn_words_table, words_proximities = \
    metrics.get_metrics_of_text(my_list, qtd_pontos_centrais)

PrintWordCloud(topn_words_table, words_proximities, qtd_pontos_centrais)