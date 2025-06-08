from calculadora_indices import calcular_calorias_en_actividad, calcular_calorias_en_reposo

while True:
    try:
        peso = float(input("Ingrese peso (Kg): "))
        altura = float(input("Ingrese altura (cm): "))
        edad = int(input("Ingrese edad (años): "))
        genero = input("Ingrese género (M para masculino, F para femenino): ").strip().upper()
        if genero == "M":
            valor_genero = 5
        elif genero == "F":
            valor_genero = -161
        else:
            print("Error: Ingrese 'M' para masculino o 'F' para femenino.\n")
            continue

        Tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
        print("\nSeleccione su nivel de actividad física:")
        print("1. Poco o ningún ejercicio → 1.2")
        print("2. Ejercicio ligero (1 a 3 días/semana) → 1.375")
        print("3. Ejercicio moderado (3 a 5 días/semana) → 1.55")
        print("4. Deportista (6 a 7 días/semana) → 1.725")
        print("5. Atleta (entrenamientos mañana y tarde) → 1.9")

        opcion = input("Ingrese el número de la opción (1-5): ")

        if opcion == "1":
             valor_actividad = 1.2
        elif opcion == "2":
            valor_actividad = 1.375
        elif opcion == "3":
            valor_actividad = 1.55
        elif opcion == "4":
            valor_actividad = 1.725
        elif opcion == "5":
            valor_actividad = 1.9
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 5.\n")
            continue
        Tmb_actividad_fisica = calcular_calorias_en_actividad(Tmb, valor_actividad)
        print (f"Las calorias que usted quema realizando actividad fisica semanalmente es: {round(Tmb_actividad_fisica, 2)} cal")
        break

    except ValueError as e:
        print(f"\nError: {e}\nPor favor, vuelva a ingresar los datos.\n")
