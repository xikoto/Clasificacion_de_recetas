import sys, os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)
from UTIL.progressBar import printProgressBar

import json
import pickle
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

stemmer = SnowballStemmer('spanish')

print("Leyendo fichero de recetas...")
with open('../DATOS/recetas.json') as recetas_file:
    recetas = json.load(recetas_file)



print("Tratamiento de texto para toda receta...");
i=0
l=len(recetas)
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

palabras = set()
for receta in recetas:

    # dietLabels
    if 'nutrition' in receta:
        palabras.update( receta['nutrition']['dietLabels'] )

    # title
    titulo = receta['title']
    if titulo is not None:
        palabras.update( titulo.strip().split() )

    # Tiempo preparación
    if 'Tiempo de preparaci\u00f3n' in receta:
        palabras.update( receta['tips']['Tiempo de preparaci\u00f3n'].strip().split() )

    # dificultad
    if 'Dificultad' in receta:
        palabras.update( receta['tips']['Dificultad'].strip().split() )

    # instrucciones
    instrucciones = receta['instructions']
    for instruccion in instrucciones:
        palabras.update( receta['instructions'][instruccion].strip().split() )

    i += 1
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

print("Quitando stopwords...")
palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords.words('spanish')]

print("Stemizando...")
palabras_stemizadas = [stemmer.stem(palabra) for palabra in palabras_filtradas]

print("Ordenando...")
palabras_stemizadas.sort()
print("Guardando...")
pickle.dump(palabras_stemizadas, open('../DATOS/BoW_texto_receta.pickle','wb'))
