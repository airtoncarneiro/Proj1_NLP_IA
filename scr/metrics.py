from math import log
import pandas as pd
import numpy as np
from itertools import chain
from collections import Counter

from pyparsing import col


def _return_counter(a_lists:list)->list:
    '''
    Retorna a quantidade de ocorrencias.
    Parameter:
      a_lists (list) Lista de palavras.
    Return:
      (list) Lista de ocorrencias.
    '''
    
    counterize = []
    for a_list in a_lists:
        count = Counter(a_list)
        counterize.append(count)
    return counterize

def _return_unique_words(a_lists:list)->set:
    '''
    Transforma a lista num objeto set (para excluir os termos repetidos).
    Parameter:
      a_lists (list) Lista de palavras de todos os documentos.
    Return:
      (set) Lista de palavras de todos os documentos sem repetição.
    '''

    words = sorted(set(list(chain(*a_lists))))
    return words

def _get_tf(word, words_tot_per_doc)->list:
    '''
    Calcula o TF.
    Parameters:
      word (str) A palavra que se quer achar o TF.
      words_tot_per_doc (list) List de palavras e seus pesos no documento.
    Return:
      (list) Lista de TFs da palavra
    '''

    tfs_list = []
    tf = 0
    for words_in_doc in words_tot_per_doc:
        calc = words_in_doc.get(word, 0) / len(words_in_doc)
        if calc > 0.0: tfs_list.append(calc)
    
    average = sum(tfs_list) /  len(tfs_list)
    return [average]

def _get_df(word:str, words_tot_per_doc):
    '''
    Calcula o DF.
    Parameters:
      docs (list) Lista com todas as palavras dos documentos.
      df (float) DF
    Return:
      (float) IDF
    '''

    idf = 0
    for doc in words_tot_per_doc:
        idf += doc.get(word, 0)
    
    return idf

def _get_idf(docs:list, df:float)->float:
    '''
    Calcula o IDF.
    Parameters:
      docs (list) Lista com todas as palavras dos documentos.
      df (float) DF
    Return:
      (float) IDF
    '''

    calc = len(docs) / (df + 1)
    return log(calc)

def _get_tfidf(idf:float, tfs:list)->list:
    '''
    Calcula o TF-IDF.
    Parameters:
      idf (float) IDF.
      tfs (list) TFs das palavras.
    Return:
      (list) Uma lista de TF-IDF
    '''

    tfidf = []
    for tf in tfs:
        tfidf.append(idf * tf)

    return tfidf

def _fill_table(a_lists:list)->pd.DataFrame:
    '''
    Preenche a tabela com as métricas.
    Parameter:
      a_lists (list) Lista com todas as palavras por documento.
    Return:
      (Dataframe) Dataframe com todas as palavras de todos os documentos
                  e suas métricas TF, DF, IDF, TF-IDF.
    '''

    tmp_df = pd.DataFrame(columns=['WORD', 'TF', 'DF', 'IDF', 'TFIDF'])

    word_count_per_doc = _return_counter(a_lists)
    unique_words = _return_unique_words(a_lists)

    for word in unique_words:
        tfs = _get_tf(word, word_count_per_doc)
        df = _get_df(word, word_count_per_doc)
        idf = _get_idf(a_lists, df)
        tfidfs = _get_tfidf(idf, tfs)

        row = {'WORD':word, 'TF':tfs, 'DF':df, 'IDF':idf, 'TFIDF':tfidfs}
        tmp_df = tmp_df.append(row, ignore_index=True)
    
    return tmp_df

def _normalize(x:float)->float:
    '''
    Normaliza os números para deixar dentro de um intervalo melhor.
    Parameter:
      x (float) Número a ser normalizado.
    Return:
      (float) Número normalizado.
    '''

    return 1 / (1 + np.exp(-x))

def _get_topn_words_tfidf(topn:int, df:pd.DataFrame)->dict:
    '''
    Retorna as top n palavras com base na métrica tf-idf.
    Parameters:
      topn (int) Informa o número TOP que se quer pegar.
      df (DataFrame) Dataframe contendo a tabela de métricas.
    Return:
      (dict) Dicionário com as top n palavras e sua métrica.
    '''

    tmp_df = pd.DataFrame(columns=['WORD', 'TFIDF'])
    for _, row in df.iterrows():
        max_value = None
        for tfidf in row['TFIDF']:
            if max_value:
                max_value = tfidf if tfidf > max_value else max_value
            else:
                max_value = tfidf
        
        new_row = {'WORD':row['WORD'], 'TFIDF':_normalize(max_value)}
        tmp_df = tmp_df.append(new_row, ignore_index=True)
    
    tmp_df = tmp_df.sort_values(by=['TFIDF'], ascending=False)[:topn]
    tmp_df.reset_index(drop=True, inplace=True)

    tmp_dict = {}
    for _, row in tmp_df.iterrows():
        tmp_dict[row['WORD']] = row['TFIDF']

    return tmp_dict

def _find_neighbors_words(words:list, docs:list, neighb:int=2)->dict:
    '''
    Procura pelas n palavras mais próximas de uma passada.
    Parameters:
      words (list): Lista de palavra centrais.
      docs (list): Lista de documentos.
      neighb (int): Informa a quantidade de palavras vizinhas que se quer pegar.
    Return:
      (dict) Dicionário com as palavras centrais como chaves e suas respectivas
             palavras vizinhas.
    '''

    a_list = {}
    for word in words:
        for doc in docs:
            indices = [i for i, x in enumerate(doc) if x == word]
            words = []
            for idx in indices:
                minIdx = idx - neighb
                if minIdx < 0: minIdx =0
                maxIdx = idx + neighb
                words = doc[minIdx:maxIdx+1]
            if words:
                words = set(words)
                words.remove(word)
                words = list(words)
            
            if words: a_list[word]=words
    
    return a_list

def _save_csv(df:pd.DataFrame)->None:
    '''
    Salva as métricas na pasta padrão
    Parameter: df (DataFrame) Dataframe (tabela) contendo as métricas.
    '''
    
    file_path = './data/processed/all_words_and_metrics.csv'
    df.to_csv(file_path, sep=';', index=False)


def get_metrics_of_text(a_lists:list, topn:int):
    '''
    Calcula as métricas TF, DF, TF-IDF, palavras vizinhas
    Parameters: a_list (list) Lista de palavras por documento
                topn (int) A quantidade (top n) de palavras.
    Return: duas listas (uma é as top n palavras e a outra
            é a que contém as n palavras próximas).
    '''

    # tabela com a lista de todas as palavras
    # e suas métricas TF, DF, IDF, TFIDF
    words_table_metrics = _fill_table(a_lists)

    # tabela com as palavras top n e seus TF-IDFs
    topn_words_table = _get_topn_words_tfidf(topn, words_table_metrics)

    # dicionário com as top n palavras e suas
    # palavras vizinhas
    words_proximities = _find_neighbors_words(list(topn_words_table.keys()), a_lists, 2)
    #words_proximities = _find_neighbors_words(topn_words_table['WORD'], a_lists, 2)


    _save_csv(words_table_metrics)

    return topn_words_table, words_proximities