print("--- Calculadora de Promedios V2 ---")

nota1 = float(input("Ingrese nota 1 (10%): "))
nota2 = float(input("Ingrese nota 2 (20%): "))
nota3 = float(input("Ingrese nota 3 (30%): "))
nota4 = float(input("Ingrese nota 4 (40%): "))

promedio = (nota1 * 0.10) + (nota2 * 0.20) + (nota3 * 0.30) + (nota4 * 0.40)

print(f"El promedio ponderado es: {promedio}")