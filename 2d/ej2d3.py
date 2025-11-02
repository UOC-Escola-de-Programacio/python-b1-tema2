from typing import List

"""
Enunciado:
Corrige la función 'division_list' que realiza una división de una lista
de número enteros dividido para un número escalar.

Para corregir los errores se puede cambiar los valores de la lista
'list_numbers' y el valor del número escalar 'scalar_number'.

En la función 'division_list' se debe verificar que el contenido de
la lista sea de tipo 'int' o 'float', caso contrario, mostrar una
excepción TypeError(f"Value {number_in_list} is not numeric.").

Parámetros:
    list_numbers (list): Lista de números.
    number (int): Número entero.
    
Ejemplos:
    Entrada:
        list_numbers = [1.5, 2.5, 9.2, 0, 22]
        scalar_number = 4.0
        
    Salida:
        [0.375, 0.625, 2.3, 0.0, 5.5]


Enunciat:
Corregeix la funció 'division_list' que fa una divisió d'una llista
de nombre enters dividit per a un nombre escalar.

Per corregir els errors es poden canviar els valors de la llista
'list_numbers' i el valor del número escalar 'scalar_number'.

A la funció 'division_list' s'ha de verificar que el contingut de
la llista sigui de tipus 'int' o 'float', en cas contrari, mostra una
excepció TypeError(f"Value {number_in_list} is not numeric.").

Paràmetres:
     list_numbers (list): Llista de números.
     number (int): Número sencer.
    
Exemples:
     Entrada:
         list_numbers = [1.5, 2.5, 9.2, 0, 22]
         scalar_number = 4.0
        
     Sortida:
         [0.375, 0.625, 2.3, 0.0, 5.5]

"""


from typing import List

def division_list(list_numbers: List, number: int) -> List[float]:
    result = []
    number_converted=0

    # check of number parameter to convert it to number if it is string
    # or if it is a letter, as well if it is empty or a list is passed
    if isinstance(number, list):
        raise TypeError(f"Value {number} is not numeric.")

    if isinstance(number, str): 
        if len(number) == 0:
            raise TypeError(f"Value {number} is not numeric.")
        if number.isalpha():
            raise TypeError(f"Value {number} is not numeric.")
        if "." in number:
            number=float(number)
        else:
            number=int(number)

    for number_in_list in list_numbers:
        if isinstance(number_in_list, int) or isinstance(number_in_list, float):
            result.append(number_in_list / number)
        if isinstance(number_in_list, str):
            raise TypeError(f"Value {number_in_list} is not numeric.")
    return result


#list_numbers = [1.5, 2.5, 9.2, 0, 22]
#scalar_number = 4.1
#scalar_number = "4.1"
#scalar_number = ""
#scalar_number = []
#scalar_number = 2
#print(division_list(list_numbers, scalar_number))

#list_numbers = [1, "a", 9, 0, 22]
#scalar_number = 2
#print(division_list(list_numbers, scalar_number))


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(division_list(list_numbers, scalar_number))
