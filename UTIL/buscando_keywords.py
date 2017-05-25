import sys, os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)

import json
from UTIL.progressBar import printProgressBar


recetasEtiquetadas = []
print("Leyendo fichero json...")
with open('../DATOS/recetas.json') as recetas_file:
    recetas = json.load(recetas_file)

    print('Buscando recetas etiquetadas...')
    i=0
    l=len(recetas)
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    keywords = set()
    for receta in recetas:

        if 'keywords' in receta:
            keyword = receta['keywords']
            if len(keyword) != 0:
                keywords.update(keyword)


        i += 1
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    print(keywords)
    for coso in keywords:
        print(coso)
