from calculadora_indices import consumo_calorias_recomendado_para_adelgazar, calcular_calorias_en_reposo

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
        consumo_recomendado = consumo_calorias_recomendado_para_adelgazar(Tmb)
        print(consumo_recomendado)
        break
    except ValueError as e:
        print(f"\nError: {e}\nPor favor, vuelva a ingresar los datos.\n")