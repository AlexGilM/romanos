#1. Crear una función # type: ignore
#2. La función recibe un parámetro
#3. Validar que la entrada reciba es un número entero
#    3.1 tiene que ser mayor que cero
#    3.2 Tiene que ser menor que 4000
#4. Devuelve una cadena


def convertir_a_romano(numero):

    #validaciones
    if type(numero) != int:
        return f'Error:  {numero}  no es un entero'
    elif numero <= 0 or numero >=4000:
        return f'Error: {numero} fuera de rango 0> # <4000'   
    
    #definiciones
    millares = ['', 'M', 'MM', 'MMM']
    centenas = ['','C','CC','CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    decenas = ['', 'X','XX', 'XXX', 'XL', 'L', 'LX', 'LXX','LXXX', 'XC']
    unidades = ['', 'I','II','III','IV','V','VI','VII','VIII','IX']
    
    #inicializacion
    romano = ''

    #calculos
    #cociente = numero // 1000
    #for i in range(cociente):
        #romano= romano + "M"

    num_millares = numero // 1000
    romano = romano + millares[num_millares]
    
    resto = numero % 1000
    num_centena = resto // 100
    romano = romano + centenas[num_centena]

    resto = numero % 100
    num_decena = resto // 10
    romano = romano + decenas[num_decena]

    resto = numero % 10
    num_unidad = resto // 1
    romano = romano + unidades[num_unidad]

    #devolvemos resultado
    return romano


# 3xx CCC...
# 4.. CD
# 5.. D  
# 6.. DC
# 7.. DCC
# 8.. DCCC
# 9.. CM
print(1137, convertir_a_romano(1137))
print(2156, convertir_a_romano(2156))
print(3256, convertir_a_romano(3256))
print(156, convertir_a_romano(156))
print(256, convertir_a_romano(256))
print(456, convertir_a_romano(456))
print(556, convertir_a_romano(556))
print(856, convertir_a_romano(856))
print(56,convertir_a_romano(56))
print(5, convertir_a_romano(5))
print(1, convertir_a_romano((1)))
print(3999, convertir_a_romano((3999)))

#print(convertir_a_romano((1,)))
#print(convertir_a_romano((0)))
#print(convertir_a_romano((4000)))

