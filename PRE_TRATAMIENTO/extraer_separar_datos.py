import sys, os
parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(path)

import json
from UTIL.progressBar import printProgressBar
import math

boca = set(['bocadillos / sándwich'])
bocaEvit = set(['segundo plato', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas'])

entra = set(['entrantes', 'aperitivos / entrantes / tapas', 'tapas'])
entraEvit = set(['segundo plato', 'bocadillos / sándwich', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas'])

primPlat = set(['primer plato,guarnición y salsas', 'primer plato'])
primPlatEvit = set(['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'segundo plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas'])

segPlat = set(['segundo plato'])
segPlatEvit = set(['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas'])

post = set(['bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas'])
postEvit = set(['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'segundo plato'])

print("Leyendo fichero json...")
with open('../DATOS/recetas_etiquetadas.json') as recetas_file:
    recetas = json.load(recetas_file)

    bocadillos = []
    entrantes = []
    primPlatos = []
    segPlatos = []
    postres = []

    print('Buscando bocadillos, entrantes, prim platos, seg patos, postres...')
    i=0
    l=len(recetas)
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for receta in recetas:
        keyword = receta['keywords']
        keyword = [key.lower() for key in keyword]
        keyword = set(keyword)

        if (( len(boca.intersection(keyword))) != 0) and (len(bocaEvit.intersection(keyword)) == 0 ):
            bocadillos.append(receta)
        elif (( len(entra.intersection(keyword))) != 0) and (len(entraEvit.intersection(keyword)) == 0 ):
            entrantes.append(receta)
        elif (( len(primPlat.intersection(keyword))) != 0) and (len(primPlatEvit.intersection(keyword)) == 0 ):
            primPlatos.append(receta)
        elif (( len(segPlat.intersection(keyword))) != 0) and (len(segPlatEvit.intersection(keyword)) == 0 ):
            segPlatos.append(receta)
        elif (( len(post.intersection(keyword))) != 0) and (len(postEvit.intersection(keyword)) == 0 ):
            postres.append(receta)

        i += 1
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    print('Separando un 0.1 del tamanyo de cada clase para el test final...')

    tamTest = 0.1
    nBoca = math.floor(len(bocadillos)*tamTest)
    nEntra = math.floor(len(entrantes)*tamTest)
    nPrimPlat = math.floor(len(primPlatos)*tamTest)
    nSegPlat = math.floor(len(segPlatos)*tamTest)
    nPost = math.floor(len(postres)*tamTest)

    bocadillosTest = bocadillos[0:nBoca]
    bocadillos = bocadillos[nBoca:]

    entrantesTest = entrantes[0:nEntra]
    entrantes = entrantes[nEntra:]

    primPlatosTest = primPlatos[0:nPrimPlat]
    primPlatos = primPlatos[nPrimPlat:]

    segPlatosTest = segPlatos[0:nSegPlat]
    segPlatos = segPlatos[nSegPlat:]

    postresTest = postres[0:nPost]
    postres = postres[nPost:]

    test = bocadillosTest + entrantesTest + primPlatosTest + segPlatosTest + postresTest
    print(str(len(test)) + ' recetas para el test final.')

    train = bocadillos + entrantes + primPlatos + segPlatos + postres
    print(str(len(train)) + ' recetas para el training.')

    print('Guardando lista en DATOS/recetas_test.json ...')
    with open('../DATOS/recetas_test.json', 'w') as outfile:
        json.dump(test, outfile)

    print('Guardando lista en DATOS/recetas_train.json ...')
    with open('../DATOS/recetas_train.json', 'w') as outfile:
        json.dump(train, outfile)
