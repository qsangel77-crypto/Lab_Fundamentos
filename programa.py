print("--- Calculadora de Promedios V4 ---")

n = int(input("¿Cuántas notas desea ingresar?: "))
suma = 0

for i in range(n):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota

promedio = suma / n

print(f"\nEl promedio es: {promedio}")

if promedio >= 12:
    print("Estado: ¡Aprobado!")
else:
    print("Estado: Reprobado")