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
    for receta in recetas:

        if 'keywords' in receta:
            if len(receta['keywords']) != 0:
                recetasEtiquetadas.append(receta)


        i += 1
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

print('Se han encontrado ' + str(len(recetasEtiquetadas)) + ' recetas etiquetadas de un total de ' + str(l) + ' recetas.' )
print('Guardando lista en DATOS/recetas_etiquetadas.json ...')
with open('../DATOS/recetas_etiquetadas.json', 'w') as outfile:
    json.dump(recetasEtiquetadas, outfile)
