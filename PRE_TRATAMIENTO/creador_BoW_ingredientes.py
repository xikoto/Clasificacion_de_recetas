import sys, os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)
from UTIL.progressBar import printProgressBar

import json
import pickle

print("Leyendo fichero de ingredientes...\n")
with open('../DATOS/ingredientes.json') as ingredientes_file:
    ingredientes = json.load(ingredientes_file)
ingredientes_file.close()

print("Preparando IDs recetas...\n");
i=0
l=len(ingredientes)
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

setIngred = set()
for ingrediente in ingredientes:
    setIngred.add(ingrediente['_id']['$oid'])

    i += 1
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


listIngred = list(setIngred)
listIngred.sort()

print("Guardando BoW en:  DATOS/BoW_ingredientes.pickle ")
with open('../DATOS/BoW_ingredientes.pickle', 'wb') as handle:
    pickle.dump(listIngred, handle)
handle.close()
