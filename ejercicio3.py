
numero = int(input("Ingrese un número entero positivo: "))


if numero < 0:
    print("El número ingresado no es positivo.")
else:
    
    cuenta_atras = [str(i) for i in range(numero, -1, -1)]
    
    resultado = ", ".join(cuenta_atras)
    
    print(resultado)
