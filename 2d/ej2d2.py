"""
Enunciado:
Implementa la función 'calculate_max_and_min' que reciba como parámetro una
lista de números 'list_numbers', se deben considerar los casos en los que los
datos que se encuentran dentro de la lista sean de type string o que la lista
se encuentre vacía. 

Adicionalmente, la función debe ir imprimiendo cual es el número menor y el
número mayor según va avanzando en la lista siempre y cuando este sea distinto
al anterior resultado simulando la depuración por trazas.

Y finalmente, retornar un valor del número menor y del número mayor.

Parámetros:
list_numbers: Lista de números.

Ejemplo:
    Entrada: 
        [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
    Salida:
        'Greater:' 200
        'Lesser: ' -55.55

    Entrada:
        ['Hello', 1, 5, -20, 55.5]
    Salida:
        TypeError

    Entrada:
        []
    Salida:
        ValueError

Enunciat:
Implementa la funció 'calculate_max_and_min' que rebi com a paràmetre una
llista de números 'list_numbers', s'han de considerar els casos en què les
dades que es troben dins de la llista siguin de tipus string o que la llista
estigui buida.

Addicionalment, la funció ha d'anar imprimint quin és el name menor i el
name més gran segons va avançant a la llista sempre que aquest sigui diferent
a l'anterior resultat simulant la depuració per traces.

I finalment, retornar un valor del name més petit i del name més gran.

Paràmetres:
list_numbers: Llista de números.

Exemple:
     Entrada:
         [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
     Sortida:
         'Greater:' 200
         'Lesser: ' -55.55

     Entrada:
         ['Hello', 1, 5, -20, 55.5]
     Sortida:
         TypeError

     Entrada:
         []
     Sortida:
         ValueError

"""


def calculate_max_and_min(list_numbers):
    max=0
    min=0
    print(f"Initial values are: max: {max} min: {min}")

    if len(list_numbers) == 0:
        raise ValueError

    for elem in list_numbers:
        if isinstance(elem, str):
            raise TypeError

        if elem > max:
            max = elem
            print(f"New value for max is: {max}")
        if elem < min:
            min = elem
            print(f"New value for min is: {min}")
    
    return (min, max)
    #return "Greater: " + str(max) + "\n" + "Lesser: " + str(min)

print(
    calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
)
#print(
#    calculate_max_and_min([1, 5, -20, 55.5, 'Hello'])
#)
#print(
#    "\nResult: \n", calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
#)



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# print(
#     "\nResult: ", calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
# )
