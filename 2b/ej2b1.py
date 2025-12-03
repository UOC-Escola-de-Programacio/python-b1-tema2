"""
Enunciado:
Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función 'sum_list_numbers', el parámetro debe ser nombrado correctamente, el
mismo debe recibir una lista.

Las buenas prácticas de programación de Python PEP8 las puedes encontrar en 
el siguiente enlace:
https://peps.python.org/pep-0008/

La función debe retornar la suma de los números encontrados en la lista.

Parámetro:
El parámetro debe recibir la siguiente lista de números y debe ser nombrado
bajo las buenas prácticas de programación. Recibe la siguiente lista:
[50, 10.5, 21, 37.2, 99.9, 40.75, 80]

Ejemplo:
    Entrada:
    sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])

    Salida:
    339.35


Enunciat:
Utilitzant les bones pràctiques de programació de Python PEP8, implementa una
funció 'sum_list_numbers', el paràmetre ha de ser nomenat correctament i 
ha de rebre una llista.

Les bones pràctiques de programació de Python PEP8 les pots trobar a
el següent enllaç:
https://peps.python.org/pep-0008/

La funció ha de retornar la suma dels números trobats a la llista.

Paràmetre:
El paràmetre ha de rebre la següent llista de números i ha de ser nomenat
sota les bones pràctiques de programació. Rep la llista següent:
[50, 10.5, 21, 37.2, 99.9, 40.75, 80]

Exemple:
     Entrada:
     sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])

     Sortida:
     339.35

"""


def sum_list_numbers(list_numbers):
    assert sum_list_numbers([1, 2, 3, 4]) == 10 "sum_list_numbers does not return the correct value for input [1, 2, 3, 4]. It should be 10"
    assert sum_list_numbers([1, 2, 3, 4, 5]) == 15 "sum_list_numbers does not return the correct value for input [1, 2, 3, 4, 5]. It should be 15"
    assert sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]) == 339.35 "sum_list_numbers does not return the correct value for input [50, 10.5, 21, 37.2, 99.9, 40.75, 80]. It should be 339.35"
def test_pep8_conformity():
    launch_path = pathlib.Path.cwd()
    exercise = "ej2b1.py"
    if str (launch_path).split(os.sep)[-1].startswith("python-b1"):
        exercise = "2b/" + exercise

    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([exercise])
    assert report.get_statistics("E") == [], "Your code does not comply with PEP8. Please review your code"
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y
# ejecuta el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

# print(sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]))
