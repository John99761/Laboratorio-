
precios_frutas = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}


fruta = input("Ingrese el nombre de la fruta: ").lower()
cantidad = float(input("Ingrese la cantidad en kilos: "))

if fruta in precios_frutas:
    
    precio_por_kilo = precios_frutas[fruta]
    total_a_pagar = precio_por_kilo * cantidad
    
 
    print(f"El total a pagar por {cantidad} kilos de {fruta} es: ${total_a_pagar:.2f}")
else:
    
    print(f"Lo siento, no tenemos {fruta} en nuestra lista.")
