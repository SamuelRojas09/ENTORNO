def es_palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    longitud: int = len(palabra)
    indice_inicio: int = 0
    indice_final: int = longitud - 1
    es_palabra_palindroma: bool = True

    while indice_inicio < indice_final:
        letra_inicio: str = palabra[indice_inicio]
        letra_final: str = palabra[indice_final]

        if letra_inicio != letra_final:
            es_palabra_palindroma = False
            break

        indice_inicio += 1
        indice_final -= 1

    return es_palabra_palindroma


palabra_usuario: str = input("Ingrese una palabra: ")
resultado: bool = es_palindromo(palabra_usuario)

if resultado:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")

"""
Definí la función es_palindromo, que recibe una palabra y la convierte a minúsculas para que la comparación no dependa de mayúsculas o minúsculas. 
Luego utilizo dos índices, uno al inicio y otro al final de la palabra, y voy comparando letra por letra mientras los índices avanzan hacia el centro.
Si encuentro alguna diferencia, la función marca que la palabra no es un palíndromo y termina la verificación. 
Después, pido la palabra al usuario con input(), llamo a la función y muestro un mensaje indicando si la palabra ingresada es o no un palíndromo.
"""