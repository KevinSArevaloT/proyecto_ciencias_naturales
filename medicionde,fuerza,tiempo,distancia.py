print("CALCULADORA DE TIEMPO (S), DISTANCIA (M) Y FUERZA(N)")
print("----------------------------------------")

continuar = "si"

while continuar.lower() == "si":

    print("\n¿Qué deseas calcular?")
    print("1. tiempo (s)")
    print("2. distancia (m)")
    print("3. fuerza (n)")

    opcion = input("Escribe 1, 2 o 3: ")

    if opcion == "1":
        # Calcular tiempo
        distancia = float(input("Ingrese la distancia (m): "))
        fuerza = float(input("Ingrese la fuerza (n): "))
        
        tiempo = distancia / fuerza
        
        print("El tiempo (s) es:", tiempo)

    elif opcion == "2":
        # Calcular distancia
        fuerza = float(input("Ingrese la fuerza (n): "))
        tiempo = float(input("Ingrese el tiempo (s): "))
        
        distancia = fuerza * tiempo
        
        print("La distancia (m) es:", distancia)

    elif opcion == "3":
        # Calcular fuerza
        distancia = float(input("Ingrese la distancia: "))
        tiempo = float(input("Ingrese el tiempo (s): "))
        
        fuerza = distancia / tiempo
        
        print("La fuerza (n) es:", fuerza)

    else:
        print("Opción no válida")

    continuar = input("\n¿Quieres hacer otro cálculo? (si/no): ")

print("\nPrograma terminado.")