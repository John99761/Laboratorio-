
numero = int(input("Ingrese un número entero positivo: "))


if numero <= 0:
    print("El número ingresado no es positivo.")
else:
   
    for i in range(1, numero + 1):
        print('*' * i)
