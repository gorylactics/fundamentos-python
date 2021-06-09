#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def big():
    lista  = [- 1, 3, 5, -5]
    for x in range(len(lista)):
        lista[x]
        if lista[x] > 1:
            lista[x] = 'big'
    return lista

llamado = big()
print(llamado)

#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
# (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def positivos():
    lista = [1,6, -4, -2, -7, -2]
    contador = 0
    for x in range(len(lista)):
        if lista[x] < 1:
            contador = contador+1
    lista[x] = contador
    return lista

print(positivos())

#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def total():
    lista = [1,2,3,4]
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma
print(total())

#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio():
    lista =[1,2,3,4]
    suma = 0
    average = 0
    for x in range(len(lista)):
        suma = suma+lista[x]
    average = suma / len(lista)
    return average
print(promedio())

#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def longitud():
    lista = [37,2,1, -9]
    if lista == []:
        return 0
    else:
        return len(lista)
print(longitud())

#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

def minimo():
    lista = [37,2,1, -9 , -5]
    mini = lista[0]
    if lista == []:
        return False
    else:
        for x in range(len(lista)):
            if mini > lista[x]:
                mini = lista[x]
        return mini
print(minimo())

#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False

def maximo():
    lista = [37,2,1, 100 ,-9]
    maxi = lista[0]
    if lista == []:
        return False
    else:
        for x in range (len(lista)):
            if maxi < lista[x]:
                maxi = lista[x]
        return maxi
print(maximo())

#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def diccionario():
    lista = [37,2,1, -9]
    suma = 0
    promedio = 0
    mini = lista[0]
    maxi = lista[0]
    longitud = len(lista)
    dicci = {}
    for x in range(len(lista)):
        suma = suma + lista[x]
        if lista == []:
            return False
        elif mini > lista[x]:
            mini = lista[x]
        if lista == []:
            return False
        elif maxi < lista[x]:
            maxi = lista[x]
    promedio = suma / len(lista)
    dicci = {f'la suma es: {suma} , el promedio es: {promedio} , el minimo es: {mini} , el maximo es: {maxi} y la longitud de la lista es: {longitud}'}
    return dicci
print(diccionario())


#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]


def invertido():
    lista = [37,2,1, -9]
    largo = (len(lista)-1) #con -1 indico el ultimo indice , con -2 el penultimo y asi sucesivamente
    modificado = int(largo/2) #como el largo esta siendo divido y da un decimal (float) , se debe transformar a un entero
    for x in range (0, modificado , 1):
        temp = lista[largo] # aca estoy accediendo al ultimo elemento -9
        lista[largo] = lista[x] #aca accedo al primer elemento por la iteracion en la cual esta 37
        lista[x] = temp
        print(lista[x])
        return lista
print(invertido())
