"""Caso 2 de Centinela"""

print("------------------------------------")
print("----------Pares e impares-----------")
print("------------------------------------")
print("                                                                 ZzzzZZzz")

#Input
n = int(input("Digite un numero: "))
    
#Processing
par = 0
impar = 0

while n != 0:
    r = n%2
    if r == 0:
        par = par + 1
    else:
        impar = impar + 1

#Input
    n = int(input("Digite un numero: "))
else:
    print("Fin de los datos de entrada")

#Output
print("Son numeros pares: " + str(par) + " numeros " + " e impares: " + str (impar) + " numeros")