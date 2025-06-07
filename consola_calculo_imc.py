from calculadora_indices import calcular_IMC 

while True:
    try:
        peso = float(input("Ingrese peso (Kg): "))
        altura = float (input("Ingrese altura (Metros): "))
        resultado = calcular_IMC (peso,altura)

        print (f"El imc es: {round(resultado,2)}")

        if resultado < 16:
            print("Categoria: Delgadez Severa")
        elif resultado < 17:
            print ("Categoria: Delgadez Moderada")
        elif resultado <18.50:
            print ("Categoria: Delgadez Aceptable")
        elif resultado < 25:
            print ("Categoria: Peso Normal")
        elif resultado <30:
            print ("Categoria: Sobrepeso")
        elif resultado < 35:
            print ("Categoria: Obesidad Tipo 1")
        elif resultado <40:
            print ("Categoria: Obesidad Tipo 2")
        elif resultado < 50:
            print ("Categoria: Obesidad Tipo 3 o morbida")
        else:
            print ("Categoria: Obesidad Tipo 4 o extrema")
        break
    except ValueError as e:
        print(f"\nError: {e}\nPor favor, vuelva a ingresar los datos.\n")