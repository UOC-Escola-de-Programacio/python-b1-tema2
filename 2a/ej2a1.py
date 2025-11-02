"""
Enunciado:
Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces 
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones 'sum_even_numbers_in_list_while(list_numbers)', 
'sum_even_numbers_in_list_for(list_numbers)' y
'sum_even_numbers_in_list_do_while(list_numbers)' en donde su parámetro
sea una lista de números y utilice un bucle 'WHILE', 'FOR' y 'DO WHILE', respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

Parámetros:
    list_numbers (List): lista de precios que se desea sumar

Ejemplo:
    Entrada:
    shopping_list = [10, 449, 33, 44, 188, 640]
    sum_even_numbers_in_list_while(shopping_list)
    sum_even_numbers_in_list_for(shopping_list)
    sum_even_numbers_in_list_do_while(shopping_list)

    Salida:
    En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640. 


Enunciat:
Una botiga té una promoció que aplica el descompte del 10% als productes
el valor numèric del qual sigui parell. Per això es requereix implementar funcions 
per sumar una llista de valors parells i retornar aquesta suma.

Implementa les funcions 'sum_even_numbers_in_list_while(list_numbers)',
'sum_even_numbers_in_list_for(list_numbers)' i
'sum_even_numbers_in_list_do_while(list_numbers)' on el paràmetre
sigui una llista de números i utilitzi un bucle 'WHILE', 'FOR' i 'DO WHILE', respectivament,
per a la seva implementació. Totes les funcions han de retornar la suma dels números parells.

Paràmetres:
     list_numbers (List): llista de preus que es vol sumar

Exemple:
     Entrada:
     shopping_list = [10, 449, 33, 44, 188, 640]
     sum_even_numbers_in_list_while(shopping_list)
     sum_even_numbers_in_list_for(shopping_list)
     sum_even_numbers_in_list_do_while(shopping_list)

     Sortida:
     En tots tres casos el resultat és 882, que és la suma de 10, 44, 188 i 640.
"""


def sum_even_numbers_in_list_while(shopping_list):
    total=0
    index_list=0
    
    # 0 index base, cal comptar la longitud menys 1, que 
    # són el número d'elements de la llista
    while index_list <= len(shopping_list)-1:
        # valor parell
        if shopping_list[index_list] % 2 == 0:
            # acumulem
            total=total+shopping_list[index_list]
        index_list +=1
    return total


def sum_even_numbers_in_list_for(shopping_list):
    total=0
    for elem in shopping_list:
        # valor parell
        if elem % 2 == 0:
            # acumulem
            total=total+elem
    return total


def sum_even_numbers_in_list_do_while(shopping_list):
    total=0
    index_list=0
    
    # 0 index base, cal comptar la longitud menys 1, que 
    # són el número d'elements de la llista
#    while index_list <= len(shopping_list)-1:
    while True:
        # valor parell
        if shopping_list[index_list] % 2 == 0:
            # acumulem
            total=total+shopping_list[index_list]
        if index_list < len(shopping_list)-1:
            index_list +=1
        else:
            break

    return total


print(sum_even_numbers_in_list_while([1, 2, 3, 4, 5, 6]))
print(sum_even_numbers_in_list_while([1, 3, 5.0, 7, 9, 10.0]))
print(sum_even_numbers_in_list_while([]))
print(sum_even_numbers_in_list_for([2, 4, 6, 8, 10]))
print(sum_even_numbers_in_list_for([3, 4, 11, 8, 10]))
print(sum_even_numbers_in_list_for([1.0, 4, 6, -3, 10]))
print(sum_even_numbers_in_list_do_while([-2, 0, 2]))
print(sum_even_numbers_in_list_do_while([6.0, 0, -2]))
print(sum_even_numbers_in_list_do_while([1, 0, 8, 3, 10]))


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# shopping_list = [10, 449, 33, 44, 188, 640]
# print(sum_even_numbers_in_list_while(shopping_list))
# print(sum_even_numbers_in_list_for(shopping_list))
# print(sum_even_numbers_in_list_do_while(shopping_list))
