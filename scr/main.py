from preprocess_file import get_preprocessed_files
from lemmatizer import Lemmatizer

preprocess_files = get_preprocessed_files()

lemma = Lemmatizer(preprocess_files)

text_lemmatized = lemma.get_all_texts_lemmatized()



