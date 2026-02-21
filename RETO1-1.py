def opereraciones(number_1: int, number_2: int, caracter: str):

    if caracter == "+":
        resultado = number_1 + number_2
        return resultado
    elif caracter == "-":
        resultado = number_1 - number_2
        return resultado
    elif caracter == "*":
        resultado = number_1 * number_2
        return resultado
    elif caracter == "/":
        if number_2 != 0:
            resultado = number_1 / number_2
            return resultado
        else:
            return "Error: no se puede dividir entre cero"
    else:
        return "Ingreso un caracter invalido"


number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
caracter = input("Ingre el signo de la operaciones que desea realizar (+, -, *, /): ")
print(opereraciones(number_1, number_2, caracter))

"""
Definí la función operaciones que recibe dos números y un operador. 
Según el operador, realiza suma, resta, multiplicación o división (verificando que no sea división entre cero). 
Si el operador es inválido, devuelve un mensaje de error. 
Luego, con input(), pido los números y el operador al usuario, y uso try-except para manejar errores si ingresa algo que no sea un número.
"""