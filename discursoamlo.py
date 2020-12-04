##Wordcloud discurso López Obrador a dos años de gobierno

##Se importa la paquetería
import pandas as pd
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from PIL import Image
from urllib.request import urlopen

##Se descarga el archivo txt de Github
data = urlopen("https://raw.githubusercontent.com/claudiodanielpc/wordclouds/main/amlosegundoinforme.txt").read()
##Se cambia el encoding
amlo=data.decode("latin1")

##Descargar stopwords
nltk.download('stopwords')
##Stopwords en español
from nltk.corpus import stopwords
stopwords_esp= set(stopwords.words('spanish'))

##Máscara de Amlo (desde Github)
mask=np.array(Image.open(urlopen("https://raw.githubusercontent.com/claudiodanielpc/wordclouds/main/amlo2.jpg")))

##Generar los colores de la wordcloud de acuerdo a la imagen
coloresimagen=ImageColorGenerator(mask)


##Se define la wordcloud

wordcloud = WordCloud(max_font_size=60, max_words=2000, 
background_color="white",width = 3000, height = 2000,
random_state=1, stopwords=stopwords_esp,
mask=mask, collocations=False).generate(amlo)


##Graficar
plt.imshow(wordcloud.recolor(color_func=coloresimagen), interpolation='bilinear')
plt.axis("off")
plt.show()

##Salvar wordcloud como png
wordcloud.to_file("amlodisc.png")