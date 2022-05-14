# quad2_atlantico
Códigos de trabalho do squad 2 Atlântico
Item 1 e 2 - Stefane e Pedrosa

item 3 e 4 - Ícaro e Leandro

item 5 e 6 - Airton e Alberlando

Priscila, Elissandra


---

# Atlântico Bootcamp - Computação Cognitiva
## Projeto I

## NLP
### Visão Geral
Uma empresa contratante deseja estabelecer termos de maior relevância em um documento específico. Neste caso, considere o histórico de exames, consultas e procedimentos realizados por um paciente. Um sistema deve ser desenvolvido para que o médico possa ter uma visão geral do histórico do paciente sem a necessidade de analisar documento por documento. Com base nesta importância, vamos desenvolver uma etapa deste sistema. Tokenizar um texto, realizar remoção de stopwords, aplicar o processo de lematização e fazer uma análise quantitativa e visual subjetiva deste.

### Objetivos
1. Carregar o conjunto de documentos em PDF e armazená-los em alguma estrutura de dados.
2. Realizar o pré-processamento destes ( tokenização e remoção de stop words, deixar todos os caracteres minúsculos...).
3. Lematização com a Lib stanza
4. Implementar para determinar as seguintes informações dos resultados obtidos em 3:
4.1 Term Frequency (TF):
&nbsp;&nbsp;&nbsp;&nbsp;𝑇𝐹 = 𝑞𝑡𝑑 𝑑𝑒 𝑜𝑐𝑜𝑟𝑟ê𝑛𝑐𝑖𝑎 𝑑𝑜 𝑡𝑒𝑟𝑚𝑜 𝑒𝑚 𝑢𝑚 𝑡𝑒𝑥𝑡𝑜 / 𝑞𝑢𝑎𝑛𝑡𝑖𝑑𝑎𝑑𝑒 𝑡𝑜𝑡𝑎𝑙 𝑑𝑒 𝑝𝑎𝑙𝑎𝑣𝑟𝑎𝑠 𝑑𝑜 𝑡𝑒𝑥𝑡𝑜
4.2 Document Frequency (DF)
&nbsp;&nbsp;&nbsp;&nbsp;𝐷𝐹 = 𝑞𝑡𝑑 𝑑𝑒 𝑜𝑐𝑜𝑟𝑟ê𝑛𝑐𝑖𝑎 𝑑𝑜 𝑡𝑒𝑟𝑚𝑜 𝑒𝑚 𝑢𝑚 𝑐𝑜𝑛𝑗𝑢𝑛𝑡𝑜 𝑑𝑒 𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑡𝑜𝑠
4.3 Inverse Document Frequency (IDF)
&nbsp;&nbsp;&nbsp;&nbsp;𝐼𝐷𝐹 = 𝑙𝑜𝑔(𝑞𝑡𝑑 𝑑𝑒 𝑑𝑜𝑐𝑢𝑚𝑒𝑛𝑡𝑜𝑠 / (𝐷𝐹 + 1))
4.4 TF-IDF
&nbsp;&nbsp;&nbsp;&nbsp;𝑇𝐹 − 𝐼𝐷𝐹 = 𝐼𝐷𝐹 * 𝑇𝐹
4.5 Lista de strings com proximidade até 2 dos 5 termos de maior TF-IDF. Essas strings devem ser acompanhadas de seu valor de TF. Exemplo: Suponha que a lista dos 5 termos demaior TF-IDF é [ casa, carro, comida, cachorro, gato]. Carro em um uma frase pode ter pneu e banco com as palavras mais próximas. Em outra parte do texto, carro pode ter volante e cinto, como as palavras mais próximas. Neste caso, para o termo carro, as strings pneu,banco,volante,cinto] são as que devem ser armazenadas para análise.
5. Gerar um arquivo csv que possui todas as palavras de todos os documentos na primeira coluna, em que cada linha é um token. Para cada token, informe nas colunas vizinhas as informações determinadas no objetivo 4.1 até 4.4.
6. Gerar nuvem de palavras para análise visual tal como exemplo abaixo. Cada ponto central será um dos 5 termos de maior TF-IDF. As conexões são as palavras próximas obtidas em 4.5. O tamanho do círculo da palavra é baseado no TF dela. O maior círculo que conecta o termo central será normalizado para palavras de maior TF do conjunto.

![Núvem de palavras](/img/wordcloud.png)


**Tópicos de Auxílio**
https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-worlddataset-796d339a4089

**Informações sobre as métricas utilizadas**
https://www.kaggle.com/arthurtok/ghastly-network-and-d3-js-force-directed-graphs

**Atividade determinação da nuvem de palavras**
http://andrewtrick.com/stormlight_network.html