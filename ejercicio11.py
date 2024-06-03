def main():
    tamano = int(input("Ingrese el tamaño de los arreglos: "))

    
    nombres = []
    longitudes = []

    
    for i in range(tamano):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
        longitudes.append(len(nombre))

    # Mostrar los arreglos
    print("Arreglo de nombres:", nombres)
    print("Arreglo de longitudes:", longitudes)

if __name__ == "__main__":
    main()
