"""Caso 1 de Centinela"""

print("------------------------------------")
print("---------NOTAS ESTUDIANTES----------")
print("------------------------------------")
print("                                                                 Grrr...")

#Input
cod = int(input("Digite el codigo del estudiante: "))
nombre = input("Digite el nombre del estudiante: ")
if cod != 0:
    nota1 = float(input("Digite la nota del parcial No.1: "))
    nota2 = float(input("Digite la nota del parcial No.2: "))
    nota3 = float(input("Digite la nota del parcial No.3: "))
else:
    print("Fin de los datos de entrada")

#Processing
reprobados = 0

while cod != 0:
    notafinal = (nota1 + nota2 + nota3)/3
    print("El estudiante de codigo " + str(cod) + ", cuyo nombre es " + nombre + ", obtuvo una nota definitiva de " + str(notafinal))
    if notafinal < 3:
        reprobados = reprobados + 1
#Input
    cod = int(input("Digite el codigo del estudiante: "))
    nombre = input("Digite el nombre del estudiante: ")

if cod != 0:
    nota1 = float(input("Digite la nota del parcial No.1: "))
    nota2 = float(input("Digite la nota del parcial No.2: "))
    nota3 = float(input("Digite la nota del parcial No.3: "))
else:
    print("Fin de los datos de entrada")

#Output
print("Cantidad de estudaintes que reprobaron la materia: " + str(reprobados))