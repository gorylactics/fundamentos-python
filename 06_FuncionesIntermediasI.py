import random
def randInt(numMin = 0 , numMax = 100):
    #numero = random.random()
    #numero = random.random() * numMax
    #numero = random.random() * numMin
    numero = random.random() *  (numMax - numMin) +  numMin
    print(numero)
    return numero
#randInt()
#randInt(numMax = 90)
#randInt(numMin = 20)
randInt(numMin = 10 , numMax = 15)
