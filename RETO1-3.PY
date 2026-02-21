def es_primo(numero: int):
    
    if numero <= 1:
        return False

    divisor: int = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def obtener_primos(lista_numeros: list[int]):

    lista_primos: list[int] = []

    for numero in lista_numeros:
        if es_primo(numero):
            lista_primos.append(numero)

    return lista_primos


try:
    entrada: str = input("Ingrese números separados por coma (ej: 4,7,9,11,15): ")

    lista_numeros: list[int] = [
        int(numero.strip()) for numero in entrada.split(",")
    ]

    resultado = obtener_primos(lista_numeros)

    print("Lista original:", lista_numeros)
    print("Números primos:", resultado)

except ValueError:
    print("Error: debe ingresar solo números enteros separados por comas.")

"""
Primero definí la función es_primo, que recibe un número y verifica si es primo. 
Si el número es menor o igual a 1, devuelve False. 
Luego, con un bucle while, revisa si existe algún divisor desde 2 hasta la raíz cuadrada del número; si encuentra uno, devuelve False, y si no, devuelve True.
Después definí la función obtener_primos, que recibe una lista de números y recorre cada número. 
Si el número es primo (usando la función anterior), lo agrega a una nueva lista de primos.
Finalmente, pido al usuario que ingrese números separados por comas y los convierto a enteros. 
Llamo a obtener_primos con esa lista y muestro tanto la lista original como los números primos.
También agregué un try-except para manejar errores si el usuario ingresa algo que no sean números enteros.
"""