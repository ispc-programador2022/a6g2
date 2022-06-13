print("Operacion - Division: \n")
#introduccion de valores (Usuario)
while True:
    try:
        num1 = float(input("Introducir primer numero: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    break
while True:
    try:
        num2 = float(input("Introducir segundo numero: "))
    except ValueError:
        print("Debes escribir un número.")
        continue
    break

# comienzo del modulo de ejecucion de operacion
division = num1 / num2
print(num1, "/", num2)
print(f"Resultado: {division}")