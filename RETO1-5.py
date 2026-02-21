def palabras_mismos_caracteres(lista: list[str]):
    resultado: list[list[str]] = []
    usados: list[bool] = [False] * len(lista)
    indice: int = 0

    while indice < len(lista):
        if usados[indice]:
            indice += 1
            continue

        palabra_base: str = lista[indice]
        letras_base: list[str] = sorted(palabra_base)
        grupo: list[str] = [palabra_base]
        usados[indice] = True

        otro_indice: int = indice + 1
        while otro_indice < len(lista):
            if not usados[otro_indice]:
                palabra_actual: str = lista[otro_indice]
                letras_actual: list[str] = sorted(palabra_actual)
                son_iguales: bool = True

                if len(letras_base) != len(letras_actual):
                    son_iguales = False
                else:
                    posicion: int = 0
                    while posicion < len(letras_base):
                        if letras_base[posicion] != letras_actual[posicion]:
                            son_iguales = False
                            break
                        posicion += 1

                if son_iguales:
                    grupo.append(palabra_actual)
                    usados[otro_indice] = True

            otro_indice += 1

        if len(grupo) > 1:
            resultado.append(grupo)

        indice += 1

    return resultado



while True:
    entrada_usuario: str = input("Ingrese palabras separadas por espacios: ")
    palabras: list[str] = []
    partes: list[str] = entrada_usuario.split()
    posicion: int = 0

    while posicion < len(partes):
        palabra: str = partes[posicion]
        palabras.append(palabra)
        posicion += 1

    if len(palabras) == 0:
        print("Debe ingresar al menos una palabra.")
        continue

    break

resultado: list[list[str]] = palabras_mismos_caracteres(palabras)
for grupo in resultado:
    print("Palabras con los mismos caracteres:", grupo)


"""
El programa recorre todas las palabras que el usuario ingresó y busca cuáles tienen los mismos caracteres.
Primero pide las palabras con input() y usa split() para separarlas en palabras individuales.
Luego toma cada palabra como base y compara sus letras con las de todas las demás palabras que todavía no hayan sido agrupadas.
Para comparar, usa sorted() que ordena las letras de cada palabra y así verifica si tienen exactamente los mismos caracteres, letra por letra.
Para no repetir palabras en varios grupos, usa una lista que marca cuáles palabras ya fueron incluidas en algún grupo.
Si todas las letras coinciden con la palabra base, agrega esa palabra al grupo y la marca como usada.
Al final, guarda solo los grupos que tienen más de una palabra, porque esos son los que realmente comparten los mismos caracteres.
Finalmente, muestra cada grupo en pantalla, indicando cuáles palabras tienen exactamente los mismos caracteres entre sí.
"""

"""
El programa recorre todas las palabras que el usuario ingresó y busca cuáles tienen los mismos caracteres.
Primero pido las palabras con input() y uso split() para separar la cadena en palabras individuales.
Luego tomo cada palabra como base y comparo sus letras con las de todas las demás palabras que todavía no hayan sido agrupadas.
Para comparar, uso sorted() que ordena las letras de cada palabra y así puedo verificar si tienen exactamente los mismos caracteres, letra por letra.
Para no repetir palabras en varios grupos, uso una lista que marca cuáles palabras ya fueron incluidas en algún grupo. 
Si todas las letras coinciden con la palabra base, agrego esa palabra al grupo y la marco como usada.
Al final, guardo solo los grupos que tienen más de una palabra, porque esos son los que realmente comparten los mismos caracteres. 
Finalmente, muestro cada grupo en pantalla, indicando cuáles palabras tienen exactamente los mismos caracteres entre sí.
"""