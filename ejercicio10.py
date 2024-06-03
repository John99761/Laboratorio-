def rellenar_array(tamano, numero):
    """Rellena un arreglo con los múltiplos de un número."""
    array = []
    for i in range(1, tamano + 1):
        array.append(numero * i)
    return array

def mostrar_array(array):
    """Muestra los elementos de un arreglo."""
    print("Contenido del arreglo:")
    for elemento in array:
        print(elemento, end=" ")
    print()  

def main():
    tamano = int(input("Ingrese el tamaño del arreglo: "))
    numero = int(input("Ingrese el número para generar los múltiplos: "))
    
    array = rellenar_array(tamano, numero)
    mostrar_array(array)

if __name__ == "__main__":
    main()
