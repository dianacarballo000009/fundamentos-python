import numpy as np
#Crear una matriz a partir de una lista
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

#Crear una matriz de ceros
zeros = np.zeros(5)
print(zeros)

#Crear una matriz de unos
ones = np.ones(5)
print(ones)


#1.5. Operaciones con matrices

#Suma
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2

# Multiplicación
resultado = arr1 * arr2

#Broadcasting con un escalar
arr = np.array([1, 2, 3])
result = arr + 5

#Difusión de matrices unidimensionales y bidimensionales*
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2


#1.7. Técnicas avanzadas de NumPy

#Segmentación e indexación
#Ejemplo de segmentación básica:
arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# Recupera los elementos donde la condición es verdadera: [3, 4, 5]

#Indexación de matrices enteras:
arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 
# Recupera los elementos en los índices especificados: [1, 3, 5]

#Concatenación y división
#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales



import numpy as np
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#Exploración inicial de los datos 
print("Dimensiones:", consumo.ndim)                         # 2 (filas y columnas)  
print("Forma:", consumo.shape)                              # (10, 7) 10 filas y 7 columnas
print("Tipo de datos:", consumo.dtype)                      # float64 (números decimales)
print("Consumo primer hogar:", consumo[0])                  # Todos los datos de la fila 0
print("Consumo el miércoles (día 3):", consumo[:, 2])       # Todos los datos de la columna 2

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
# índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

#Aplicando normalizació MinMáx al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print(consumo_normalizado)

#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_viernes = consumo[4, 4]
print(f"1. Consumo del hogar 5 el viernes (día 5): {consumo_hogar5_viernes}")

#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
consumo_ultimos3_domingo = consumo[-3:, 6]
print(f"2. Consumo de los últimos 3 hogares el domingo: {consumo_ultimos3_domingo}")

#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
arr = consumo[:, [5, 6]] 
promedio_finde = np.mean(arr)

print(f"\n3. El promedio de consumo del fin de semana es de: {promedio_finde}")

#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion_idx = np.argmax(desviacion_por_dia)
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_mayor_desviacion = dias_semana[dia_mayor_desviacion_idx]

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
print(f"4. Día con la mayor desviación estándar entre hogares: {dia_mayor_desviacion}")

#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
arr = consumo[2]
result = arr * 1.10

nuevo_total = np.sum(result)  # Suma del nuevo consumo semanal
print(f"\n6. El nuevo consumo total semanal del hogar 3 con aumento del 10% es: {nuevo_total}")