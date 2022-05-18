



![elem3](https://user-images.githubusercontent.com/104634692/169033139-31b70a2d-d302-4150-b6ca-723dd636aa3c.png)



# Primeiro Projeto do Bootcamp do Instituto Atlântico 


### Desenvolvido pelos alunos do Squad2:
Airton, Ícaro e Leandro


## O Projeto

Para executar o projeto clone o repositório e use o pipinstall com o arquivo requirements.
Para executá-lo, abrir o main.py e rodar.
O projeto está todo customizável e adaptável. A quantidade de nós, quantas palavras vizinhas, leitura de quaisquer arquivos com extensão .PDF.
## Introdução

Projeto criado com o objetivo de apresentar, com base em NLP, uma visão geral do histórico de um paciente sem a necessidade de analisar documento por documento referentes a histórico de exames, consultas e procedimentos.



### Sumário da solução

1. [Dataset](#section01)
   
2. [Pré-processamento dos dados](#section02)
  
3. [Lematização](#section03)

4. Determinar com base nos resultados da lematização:

    4.1 Term Frequency<br>
    4.2 Document Frequency<br>
    4.3 Inverse Document Frequency<br>
    4.4 TF-IDF<br>
    4.5 𝑇𝐹 − 𝐼𝐷𝐹 = 𝐼𝐷𝐹 * 𝑇𝐹<br>
 5. Gerar um arquivo csv que possui todas as palavras de todos os documentos na primeira coluna
 6. [Resultado em Nuvem de palavras](#section04)
 7. [Tópicos de Auxílio](#section05)
   


<a id='section01'></a>
### Dataset
Como base dados foram utilizados 3 documentos com histórico de consultas no formato pdf de um paciente.

<a id='section02'></a>
### Pré-processamento dos dados
Para os dados foram aplicados processamento como tokenização e remoção de stop words e transformar os caracteres todos em minúsculos.

<a id='section03'></a>
### Lematização
Tendo os dados já processados realizou-se a lematização com a biblioteca Stanza.

<a id='section04'></a>
### Resultado em nuvem de palavras

![wordcloud](./img/wordcloud2.png)

<a id='section05'></a>
### Tópicos de Auxílio


**Tópicos de Auxílio**
https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-worlddataset-796d339a4089

**Informações sobre as métricas utilizadas**
https://www.kaggle.com/arthurtok/ghastly-network-and-d3-js-force-directed-graphs

**Atividade determinação da nuvem de palavras**
http://andrewtrick.com/stormlight_network.html
