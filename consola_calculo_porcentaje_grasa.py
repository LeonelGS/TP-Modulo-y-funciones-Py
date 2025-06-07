from calculadora_indices import calcular_IMC, calcular_porcentaje_grasa 
    

while True:
    try:
        peso = float(input("Ingrese peso (Kg): "))
        altura = float(input("Ingrese altura (Metros): "))
        edad = int(input("Ingrese edad (años): "))
        genero = input("Ingrese género (M para masculino, F para femenino): ").strip().upper()
        if genero == "M":
            valor_genero = 10.8
        elif genero == "F":
            valor_genero = 0
        else:
            print("Error: Ingrese 'M' para masculino o 'F' para femenino.\n")
            continue

        resultado = calcular_IMC(peso, altura)
        Gc = calcular_porcentaje_grasa(resultado, edad, valor_genero)

        print(f"El porcentaje de grasa corporal es: {round(Gc, 2)}%\n")
        if genero == "M":
            if 20 <= edad <= 29:
                min_gc, max_gc = 11, 20
            elif 30 <= edad <= 39:
                min_gc, max_gc = 12, 21
            elif 40 <= edad <= 49:
                min_gc, max_gc = 14, 23
            elif 50 <= edad <= 59:
                min_gc, max_gc = 15, 24
            else:
                print("Edad fuera de rango para evaluación.")
                break
        else: 
            if 20 <= edad <= 29:
                min_gc, max_gc = 16, 28
            elif 30 <= edad <= 39:
                min_gc, max_gc = 17, 29
            elif 40 <= edad <= 49:
                min_gc, max_gc = 18, 30
            elif 50 <= edad <= 59:
                min_gc, max_gc = 19, 31
            else:
                print("Edad fuera de rango para evaluación.")
                break

        if Gc < min_gc:
            print("Porcentaje de grasa corporal bajo.")
        elif Gc > max_gc:
            print("Porcentaje de grasa corporal alto.")
        else:
            print("Porcentaje de grasa corporal dentro del rango recomendado.")

        break
    except ValueError as e:
        print(f"\nError: {e}\nPor favor, vuelva a ingresar los datos.\n")
