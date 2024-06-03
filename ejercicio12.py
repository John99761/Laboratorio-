def encontrar_maximo(lista):
    """Encuentra el número más grande en una lista."""
    if not lista:
        return None  
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def main():
    
    numeros = [2, 7, 1, 9, 5, 4, 8]

    
    maximo = encontrar_maximo(numeros)

    
    print("El número más grande en la lista es:", maximo)

if __name__ == "__main__":
    main()
