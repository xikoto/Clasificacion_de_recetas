import sys, os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)

import json
from UTIL.progressBar import printProgressBar


recetasNOEtiquetadas = []
print("Leyendo fichero json...")
with open('../DATOS/recetas.json') as recetas_file:
    recetas = json.load(recetas_file)

    print('Buscando recetas NO etiquetadas...')
    i=0
    l=len(recetas)
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for receta in recetas:

        if 'keywords' not in receta:
            recetasNOEtiquetadas.append(receta)
        elif len(receta['keywords']) == 0:
                recetasNOEtiquetadas.append(receta)


        i += 1
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

print('Se han encontrado ' + str(len(recetasNOEtiquetadas)) + ' recetas no etiquetadas de un total de ' + str(l) + ' recetas.')
print('Guardando lista en recetas_NO_etiquetadas.json ...')
with open('../DATOS/recetas_NO_etiquetadas.json', 'w') as outfile:
    json.dump(recetasNOEtiquetadas, outfile)
