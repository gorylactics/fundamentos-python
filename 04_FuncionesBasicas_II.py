#1.
#Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

entrada = int(input('ingresa un numero: '))
def reversa(num):
    lista = []
    for x in range(num , -1 , -1):
        lista.append(x)
    return lista
resultado = reversa(entrada)
print(resultado)

#2
#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def numeros(num):
    print(num[0])
    return num[1]
enteros = numeros([1, 2])
print(enteros)

#3
#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.

def suma(lista):
    suma = lista[0] + len(lista)
    return suma

listado = suma([1,2,3])
print(listado)

#4
#Valores mayores que el segundo : escribe una función que acepte una lista 
# y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva
# lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False

def lista(lista):
    nuevaLista = []
    if len(lista) < 2:
        return print(False)
    else:
        for x in range(len(lista)):
            lista[x]
            if lista[x] > lista[1]:
                nuevaLista.append(lista[x])
    return nuevaLista

laLista = lista([5,2,3,2,1,4])
print(laLista)

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
#La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def longitud(tamano , valor):
    lista = []
    for x in range(tamano):
        lista.append(valor)
    return lista

largo = 5
elValor = 2
llamado  = longitud(largo ,elValor)
print(llamado)

