def mayor_suma_consecutiva(lista: list[int]):
    if len(lista) < 2:
        return 0

    suma_actual: int = lista[0] + lista[1]
    mayor_suma: int = suma_actual

    indice: int = 1

    while indice < len(lista) - 1:
        numero_actual: int = lista[indice]
        numero_siguiente: int = lista[indice + 1]

        suma_actual = numero_actual + numero_siguiente

        if suma_actual > mayor_suma:
            mayor_suma = suma_actual

        indice += 1

    return mayor_suma


while True:
    entrada_usuario: str = input("Ingrese los números separados por espacios: ")
    numeros: list[int] = []

    try:
        for num in entrada_usuario.split():
            numeros.append(int(num))  

        if len(numeros) < 2:
            print("Debe ingresar al menos dos números.")
            continue

        break 

    except ValueError:
        print("Entrada inválida. Solo ingrese números enteros separados por espacios.")

resultado: int = mayor_suma_consecutiva(numeros)
print("La mayor suma consecutiva es:", resultado)

"""
Primero definí la función es_primo, que recibe un número y verifica si es primo. Si el número es menor o igual a 1, devuelve False.
Luego, con un bucle while, revisa si existe algún divisor desde 2 hasta la raíz cuadrada del número; si encuentra uno, devuelve False, y si no, devuelve True.
Después definí la función obtener_primos, que recibe una lista de números y recorre cada número.
 Si el número es primo (usando la función anterior), lo agrega a una nueva lista de primos.
Finalmente, pido al usuario que ingrese números separados por comas y los convierto a enteros. 
Llamo a obtener_primos con esa lista y muestro tanto la lista original como los números primos. 
También agregué un try-except para manejar errores si el usuario ingresa algo que no sean números enteros.
"""
