import nltk

# desde nltk descargar stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('english')
# imprimir las stopwords
print(lista_stopwords)

#importar la libreria nltk
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.data.path.append('C:/Users/Leidy/Downloads/nltk_data')
