from heapq import nlargest
import matplotlib.pyplot as plt
import networkx as nx

class PrintWordCloud:
    def __init__(self, tf_idf:dict, tokens_and_words:dict, qtd_pnts_central:int):
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
        G.add_nodes_from(words)
        G.add_edges_from(edges)

        # Atribuindo cores e tamanhos aos nós
        node_color = ['orange' if i in words else 'skyblue' for i in G]
        node_size = [int(tamanho[node]*2000) if node in words \
            else 350 for node in G]

        # Construindo o gráfico:
        nx.draw_kamada_kawai(G, with_labels=True, \
                width=3, node_color=node_color, \
                edge_color="gray", style="solid",
                node_size=node_size)
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