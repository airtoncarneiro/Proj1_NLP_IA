import os
import glob
from collections import deque
from operator import itemgetter
import pdfplumber
from process_text import Process_Text

def _find_files()->list:
    '''
    '''

    rel_path = 'data\\raw'
    ext = '*.pdf'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = glob.glob(os.path.join(base_path, rel_path, ext))

    return files

def _read_file_content(file:str):
    '''
    '''

    contents_pages = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            contents_pages.append(page.extract_text())

    return contents_pages

def read_files(files:list)->deque:
    '''
    '''

    docs_queue = deque()
    for file in files:
        content = _read_file_content(file)
        tmp_dict = {'doc': file, 'content': content}
        docs_queue.append(tmp_dict)
    
    return docs_queue

def get_preprocessed_files():
    '''
    '''

    files = _find_files()
    if files:
        docs_contents = read_files(files)
        
        while docs_contents:
            doc_name, content = itemgetter('doc', 'content')(docs_contents.popleft())
            processed_content = Process_Text(content)
            



if __name__ == '__main__':
    get_preprocessed_files()