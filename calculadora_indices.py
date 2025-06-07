
def calcular_IMC (peso:float,altura:float)-> float:
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    return peso / altura**2



def calcular_porcentaje_grasa (resultado:float, edad:int, valor_genero:float)-> float:
    return (1.2 * resultado + 0.23 * edad - 5.4 - valor_genero)


def calcular_calorias_en_reposo (peso:float, altura:float, edad:int, valor_genero:int)-> float:
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que cero.")
    return ((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero)



def calcular_calorias_en_actividad(Tmb: float, valor_actividad: float)-> float:
    return Tmb * valor_actividad



def consumo_calorias_recomendado_para_adelgazar(Tmb: float): 
    minimo = Tmb * 0.80
    maximo = Tmb * 0.85
    return f"Para adelgazar es recomendado que consumas entre: {round(minimo, 2)} y {round(maximo, 2)} calorias al día."



