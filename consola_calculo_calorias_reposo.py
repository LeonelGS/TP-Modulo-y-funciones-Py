from calculadora_indices import calcular_calorias_en_reposo

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
        print(f"\nLas calorías que usted quema estando en reposo son: {round(Tmb, 2)} cal")
        break

    except ValueError as e:
        print(f"\nError: {e}\nPor favor, vuelva a ingresar los datos.\n")