# Tuplas
mi_tupla = (2, 4)
print("Mi tupla: ",mi_tupla)

# Lista
mi_lista = [1, 3.1416, "Christian", mi_tupla]
print("El primer elemento de mi lista:", mi_lista[0])
print("El cuarto elemento de mi lista: ", mi_lista[3])
print("El tercer elemento de mi lista: ",mi_lista[2])

#Diccionarios
mi_diccionario = {"mi_lista": mi_lista,
                  "Nombre": "Macario",
                  "pi": 3.1416,
                  "Tel": "664-200-2123"}
print("Llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("Llave para acceder a mi diccionario pi  ", mi_diccionario["pi"])
print("Llave para acceder a mi diccionario tel", mi_diccionario["Tel"])