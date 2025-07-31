# import nltk 
import nltk

# desde nltk descargar stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('russian')
# imprimir las stopwords
print(lista_stopwords)