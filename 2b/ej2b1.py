def sum_list_numbers(list_numbers):
    sum_numbers = 0     # Inicializamos la variable resultado
    for number in list_numbers:     # Pillamos cada numero de la lista
        sum_numbers += number       # Lo sumamos a resultado
    return sum_numbers      # Resultado final


list_numbers = [50, 10.5, 21, 37.2, 99.9, 40.75, 80]
print(sum_list_numbers(list_numbers))
