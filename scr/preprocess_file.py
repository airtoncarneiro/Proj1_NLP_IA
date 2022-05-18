import os
import glob
from collections import deque
from operator import itemgetter
import pdfplumber
from process_text import Process_Text

def _find_files()->list:
    '''
    Procura os arquivos na pasta padrão do projeto.

    Return: (list) Retorna a lista de arquivos encontrados.
    '''

    rel_path = os.path.join('data','raw')
    ext = '*.pdf'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = glob.glob(os.path.join(base_path, rel_path, ext))

    return files

def _read_file_content(file:str)->list:
    '''
    Lê o conteúdo do arquivo.
    Parameter: (str) Path completo do arquivo a ser lido.
    Return: (list) Lista com o conteúdo de cada página do arquivo.
    '''

    contents_pages = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            contents_pages.append(page.extract_text())

    return contents_pages

def read_files(files:list)->deque:
    '''
    Lê o conteúdo de cada arquivo da lista.
    Parameter: (list) Uma lista de arquivos (path completo).
    Return: (deque) Retorna um objeto deque com o conteúdo dos arquivos.
    '''

    docs_queue = deque()
    for file in files:
        content = _read_file_content(file)
        tmp_dict = {'doc': file, 'content': content}
        docs_queue.append(tmp_dict)
    
    return docs_queue

def get_preprocessed_files()->list:
    '''
    Lê todos os arquivos e faz o pré-processamento deles.

    Return: (list) Lista de palavras de cada documento.
    '''
    all_contents = []
    files = _find_files()
    if files:
        docs_contents = read_files(files)
        
       
        while docs_contents:
            _, content = itemgetter('doc', 'content')(docs_contents.popleft())
            processed_content = Process_Text(content)
            all_contents.append(processed_content.all_contents)
    
<<<<<<< HEAD:scr/vc/preprocess_file.py
    return all_contents
            



if __name__ == '__main__':
    print(_find_files())
=======
    return all_contents
>>>>>>> dev_a:scr/preprocess_file.py
