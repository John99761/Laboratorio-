
entrada = input("Ingrese las palabras y sus traducciones en el formato 'palabra:traducción' separadas por comas: ")


traducciones = {}
pares = entrada.split(',')

for par in pares:
    palabra, traduccion = par.split(':')
    traducciones[palabra.strip()] = traduccion.strip()


frase = input("Ingrese una frase en español: ")


palabras = frase.split()
frase_traducida = []

for palabra in palabras:
    if palabra in traducciones:
        frase_traducida.append(traducciones[palabra])
    else:
        frase_traducida.append(palabra)


frase_traducida_str = ' '.join(frase_traducida)


print("Frase traducida:", frase_traducida_str)
