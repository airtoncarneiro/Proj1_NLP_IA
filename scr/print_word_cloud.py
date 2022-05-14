from heapq import nlargest
import matplotlib.pyplot as plt
import networkx as nx

class PrintWordCloud:
    def __init__(self, qtd_pnts_central:int, tf_idf:dict, tokens_and_words:dict):
        """ Gera o gráfico de palavras

        params:
        ======
        qtd_pnts_central (int) é a quantidade de pontos
            centrais do gráfico. Ou seja, as principais
            palavras.
        tf_idf (dict) é um dicionário contendo as palavras
            como chaves e os valores como peso.
        tokens_and_words (dict) é o conjunto de todas as
            palavras do texto formado por tokens e palavras.
        """
        # Obtem as n principais palavras
        palavras_centrais = self._get_topn_words(qtd_pnts_central, tf_idf)

        # Obtem os vértices
        edges = [ (i, j[k]) \
        for i, j in tokens_and_words.items() \
                if i in palavras_centrais for k in range(len(j)) ]
        
        # Chama a plotagem
        self._plotNx(tokens_and_words, edges, tf_idf)
        pass

    def _plotNx(self, words:dict, edges:list, tamanho:dict):
        """
        """
        # Definindo a área de plotagem e instanciando NX
        plt.subplots(figsize=(12,6))
        G = nx.Graph()

        # Nodes and Edges
        G.add_nodes_from( words )
        G.add_edges_from( edges )

        # Atribuindo cores e tamanhos aos nós
        node_color = [ 'orange' if i in words else 'skyblue' for i in G ]
        # node_size = [ int(tamanho[node]*2000) if node in words else 350 for node in G ]

        # Construindo o gráfico:
        nx.draw_kamada_kawai( G, with_labels=True, \
                width=3, node_color=node_color, \
                edge_color="gray", style="solid" )
        plt.show()

    def _get_topn_words(self, top:int, tf_idf:dict) -> list:
        """Retorna os top primeiros maiores de uma lista
        com base nos seus pesos.

        params:
        ======
        top (int) Informa até qual posição ordinal se
            deseja calcular.
        tf_idf (dict) Dicionário contendo como chaves
            como chaves as palavras e valores como pesos.
        retorno:
        =======
        (list) Retorna uma lista das primeiras 'top'
            palavras.
        """
        return nlargest( top, tf_idf, key = tf_idf.get )

    # def __draw_graphic(self, qtd_pnts_central:int, tf_idf:dict, tokens_and_words:dict):
    #     """ Gera o gráfico de palavras

    #     params:
    #     ======
    #     qtd_pnts_central (int) é a quantidade de pontos
    #         centrais do gráfico. Ou seja, as principais
    #         palavras.
    #     tf_idf (dict) é um dicionário contendo as palavras
    #         como chaves e os valores como peso.
    #     tokens_and_words (dict) é o conjunto de todas as
    #         palavras do texto formado por tokens e palavras.
    #     """
    #     # Obtem as n principais palavras
    #     palavras_centrais = self._get_topn_words(qtd_pnts_central, tf_idf)

    #     # Obtem os vértices
    #     edges = [ (i, j[k]) \
    #     for i, j in tokens_and_words.items() \
    #             if i in palavras_centrais for k in range(len(j)) ]
        
    #     # Chama a plotagem
    #     self._plotNx(tokens_and_words, edges, tf_idf)

if __name__ == '__main__':
    # Este é o modelo de entrada que deve ser passado como parâmentro
    # na instanciação da classe que imprime o gráfico
    todas_palavras_e_seus_vertices = {
    'brincar': ['feliz', 'escada', 'policia', 'mundo', 'parede', 'feliz'],
    'correr': ['rua', 'parque', 'escada', 'noiva', 'aliança', 'mãe'],
    'chutar': ['ladrao', 'parede', 'irmao', 'mundo', 'parque', 'feliz'],
    'amar': ['noiva', 'esposa', 'parque', 'policia', 'esposa', 'rua'],
    'gostar': ['noiva', 'esposa', 'irmao', 'mundo', 'parede', 'porta'],
    'destruir': ['mundo', 'parede', 'porta', 'noiva', 'aliança', 'mãe'],
    'noivar': ['noiva', 'aliança', 'mãe', 'mundo', 'parque', 'feliz'],
    'matar': ['policia', 'ladrao', 'bandido', 'noiva', 'aliança', 'mãe'],
    'cair': ['rua', 'porta', 'escada', 'mundo', 'parque', 'feliz'],
    'morrer': ['policia', 'esposa', 'rua', 'mundo', 'parque', 'feliz'],
    'viver': ['mundo', 'parque', 'feliz', 'noiva', 'aliança', 'mãe'],
    'anoitecer' : ['rua', 'parque', 'irmao', 'mundo', 'parede', 'porta']
    }

    # TF-IDF
    pontos_centrais_e_seus_pesos = {
        'brincar': 0.90,
        'correr': 0.75,
        'chutar': 0.60,
        'amar': 0.45,
        'gostar': 0.30,
        'destruir': 0.11,
        'noivar': 0.10,
        'matar': 0.09,
        'cair': 0.08,
        'morrer': 0.07,
        'viver': 0.06,
        'anoitecer' : 0.05
    }

    qtd_pontos_centrais = int =  5
    PrintWordCloud(qtd_pontos_centrais, pontos_centrais_e_seus_pesos, todas_palavras_e_seus_vertices)