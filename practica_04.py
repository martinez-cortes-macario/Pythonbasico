print("==========Mi Super Calculadora==========")
def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "Error: No se puede dividir entre 0"

while True:
    operacion = input("¿Qué operación quieres hacer? (+, -, *, /) o S para salir: ").upper()
    
    if operacion == "S":
        print("Calculadora finalizada.")
        break
    
    if operacion not in ["+", "-", "*", "/"]:
        print("Operación no válida. Intenta de nuevo.")
        continue

    num_1 = float(input("Escribe el primer número: "))
    num_2 = float(input("Escribe el segundo número: "))
    
    resultado = calculadora(num_1, num_2, operacion)
    print("El resultado es:", resultado)
    print("-----------------------------")
