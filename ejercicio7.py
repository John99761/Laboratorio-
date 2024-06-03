# Crear un diccionario con las asignaturas y sus créditos
asignaturas = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5,
    "Historia": 3,
    "Literatura": 4
}

# Inicializar una variable para el total de créditos
total_creditos = 0

# Recorrer el diccionario y mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")
    total_creditos += creditos

# Mostrar el número total de créditos del curso
print(f"El número total de créditos del curso es: {total_creditos}")
