def tabla_de_multiplicar(numero):
    """Imprime la tabla de multiplicar del número dado."""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    
    numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

    
    tabla_de_multiplicar(numero)

if __name__ == "__main__":
    main()
