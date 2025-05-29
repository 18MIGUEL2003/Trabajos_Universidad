import statistics

# Lista vacía para guardar los datos
CantidadDatos = []

# Solicitar al usuario los datos
while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ").strip()

    if entrada.lower() == 'fin':
        break  # Sale del ciclo

    try:
        numero = float(entrada) # Aquí indicamos que los datos recibidos en la lista sean tipo flotantes
        CantidadDatos.append(numero) # Con esto vamos agregando los datos a la lista
    except ValueError:
        print("⚠️ Entrada no válida. Por favor ingrese un número o 'fin'.")

# Verifica que haya suficientes datos
if len(CantidadDatos) >= 2:
    print("La lista resultante es:", CantidadDatos)
    varianza = statistics.variance(CantidadDatos)
    print("Varianza:", varianza)
else:
    print("Se necesitan al menos 2 datos numéricos para calcular la varianza.")