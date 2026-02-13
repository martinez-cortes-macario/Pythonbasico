#loops

mi_lista = [1,2,3,4,5]
for i in mi_lista:
    print("el numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i

print("El resultado de la suma de mi lista es: {resultado}")

for i in range(2,8):
    print(i)

mi_lista_2 = ["lunes", "martes", "miercoles","jueves","viernes"]

for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz{i}!")

# while loop
i=0

while i<5:
    i+=1
    if i==3:
        continue
    print(i)
    if i== 4:
        break

else:
    print(" i es mayor o igual a 5")

#Practica 2
#Dada la lista mi_lista_2 = ["lunes", "martes", "miercoles","jueves","viernes"]
#Imprimir cada elmento de la lista 3 veces y cuando sea lunes no lo incluyas
#Pista: Usa los dos tipos de loops while y for en el mismo programa para lograrlo
#Resultado:
# martes
# miercoles
# jueves
# viernes
# martes
# martes
# miercoles
# jueves
# viernes
# martes
# martes
# miercoles
# jueves
# viernes
# martes
# Practica 2

contador = 0
while contador < 3:
    for dia in mi_lista_2:
        if dia != "lunes":
            print(dia)
    contador += 1
