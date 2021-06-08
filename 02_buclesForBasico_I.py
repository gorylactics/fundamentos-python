for i in range(0 ,  151 , 1):
    print(i)

for i in range(5 , 1001 , 5):
    print(i)

for i in range(1 ,101 , 1):
    if i%10==0:
        print('codingDojo')
    elif i%5==0:
        print('coding')
    else:
        print(i)

contador = 0
for i in range(0 , 100 , 1):
    if i%2==1:
        contador += i
        print(contador)

for i  in range(2018 , 0 , -4):
    print(i)

lowNow = 2
highLow = 9
mult = 3
for i in range(lowNow , highLow+1 ,1 ):
    if i%mult==0:
        print(i)

#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, 
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
#BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?
conteo = 1001
for x in range (1, conteo):
    print(x)