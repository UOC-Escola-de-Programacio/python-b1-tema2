def triangle_area_calculate(base, height):
    if base > 0 and height > 0:     # Si los valores son superiores a cero
        return 0.5 * (height * base)    # Calcula el area del triangulo
    else:       # Si los valores no son superiores a cero
        raise ValueError("El valor introducido es negativo")    # Envia error


print(triangle_area_calculate(33, 45))
