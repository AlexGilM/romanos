#1. Crear una función # type: ignore
#2. La función recibe un parámetro
#3. Validar que la entrada reciba es un número entero
#    3.1 tiene que ser mayor que cero
#    3.2 Tiene que ser menor que 4000
#4. Devuelve una cadena

def convertir_a_romano(numero):
    if type(numero) != int:
        return 'Error: no es un entero'
    return 'TODO: Convertir a romano'
print(convertir_a_romano(56))
print(convertir_a_romano(56.1))
print(convertir_a_romano('algo escrito'))
print(convertir_a_romano([]))
print(convertir_a_romano((1,)))


