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
    cont = 0

    '''#Bocadillos
    clases = ['bocadillos / sándwich']
    evitar = ['segundo plato', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas']
    #Entrantes
    clases = ['entrantes', 'aperitivos / entrantes / tapas', 'tapas']
    evitar = ['segundo plato', 'bocadillos / sándwich', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas']
    #Primer plato
    clases = ['primer plato,guarnición y salsas', 'primer plato']
    evitar = ['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'segundo plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas']
    '''#Segundo plato
    clases = ['segundo plato']
    evitar = ['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas']
    '''#Postres
    clases = ['bizcochos / pasteles / tartas / mousse,chocolate', 'bizcochos / pasteles / tartas / mousse', 'postres,bebidas']
    evitar = ['bocadillos / sándwich', 'entrantes', 'aperitivos / entrantes / tapas', 'tapas', 'primer plato,guarnición y salsas', 'primer plato', 'segundo plato']
    '''
    clases = set(clases)
    evitar = set(evitar)
    for receta in recetas:

        '''
        if 'keywords' in receta:
            keyword = receta['keywords']
            if len(keyword) != 0:
                keywords.update(keyword)
        '''
        if 'keywords' in receta:
            keyword = receta['keywords']
            keyword = [key.lower() for key in keyword]
            keyword = set(keyword)
            if ( len(clases.intersection(keyword))) != 0 and (len(evitar.intersection(keyword)) == 0 ):
                cont += 1

        i += 1
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    '''
    print(keywords)
    for coso in keywords:
        print(coso)
    '''
    print('Se han encontrado ' + str(cont) + ' recetas')
