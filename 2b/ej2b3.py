"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5


Enunciat:
Implementa una funció 'triangle_area_calculate', que rebi dos paràmetres,
que corresponen a l'alçada i la base d'un triangle i que han de
ser números positius. Aquests paràmetres han de ser nomenats correctament,
considerant les bones pràctiques de programació PEP8.
La funció ha de retornar el càlcul de l'àrea d'un triangle mitjançant les
dades introduïdes, addicionalment, el codi ha de tenir comentaris de manera
que es vagi explicant el procediment.

Paràmetres:
Són dos paràmetres, que corresponen a l'alçada i la base de
un triangle i que han de ser números positius. S'han de crear correctament
utilitzant les bones pràctiques de programació PEP8.


Exemple:
     Entrada:
     triangle_area_calculate(33, 45)

     Sortida:
     742.5

"""

"""
Generic function to check if an input parameter is greater than 0
If not, raise a ValueError exception

Parameters:
- param: numeric value to be tested
- name_param: name of parameter being tested, to be shown in case of error

Returns
- Nothing if parameter is greater than 0
- Value Error exception if parameter condition is not satisfied
"""


def checkInputParameters(param, name_param):
    if param <= 0:
        raise ValueError(name_param + " should be greater than 0")


"""
Function to calculate the area of a triangle using the following formula:
area=(base*height) / 2
Parameters:
- base: base of the triangle
- height: height of the triangle

Returns
- result: calculated triangle area
"""


def triangle_area_calculate(base, height):
    # contains the calculated area
    area = 0

    # check input parameters
    checkInputParameters(base, "base")
    checkInputParameters(height, "height")

    # apply formula
    area = (base * height) / 2

    # delete .0 from the result. For other decimals we do nothing
    # some string stuff to delete .0
    string_decimals = str(area)[-2:]
    if string_decimals == ".0":
        temp_area = int(str(area)[0:len(str(area))-2])
        # return value without ".0"
        return temp_area

    # return calculated area
    return area


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'scrip

print(triangle_area_calculate(33, 45))
