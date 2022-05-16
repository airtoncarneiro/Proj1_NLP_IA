import preprocess_file
import stannize
import metrics
from print_word_cloud import PrintWordCloud

# Lê os arquivos e faz um pré-processamento
my_list = preprocess_file.get_preprocessed_files()
# staniza a lista de palavras
my_list = stannize.get_words_stannizeds(my_list)

# informa a quantidade de pontos centrais
qtd_pontos_centrais = int =  5
# informa a quantidade de palavras vizinhas
qtd_palavras_vizinhas = 5

# Obtém a tabela de palavras e as métricas
topn_words_table, words_proximities = \
    metrics.get_metrics_of_text(my_list, qtd_pontos_centrais, \
                                qtd_palavras_vizinhas)
    
# mostra o gráfico
PrintWordCloud(topn_words_table, words_proximities, \
          qtd_pontos_centrais)