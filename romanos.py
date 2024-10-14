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
    
    conversores = [
        unidades,
        decenas,
        centenas,
        millares,     
        ]

    # conversores = [
    #     ['', 'I','II','III','IV','V','VI','VII','VIII','IX']
    #     ['', 'X','XX', 'XXX', 'XL', 'L', 'LX', 'LXX','LXXX', 'XC']
    #     ['','C','CC','CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    #     ['', 'M', 'MM', 'MMM']
    # ]

    # conversores[1][4] -----> 40 ó XL
    #1 --- conversores[3][1]
    #1 --- conversores[2][1]
    #3 --- conversores[1][3]
    #7 --- conversores[03][7]
    #range(4) ---- 1000, 1000, 10, 1 ----- 3, 2, 1, 0
    #inicializacion
    romano = ''

    #calculos
    #cociente = numero // 1000
    #for i in range(cociente):
        #romano= romano + "M"

    #cociente = numero // 10**3
    #romano = romano + conversores[3][cociente]
    #resto = numero % 10**3
    
    #cociente = resto // 10**2
    #romano = romano + conversores[2][cociente]
    #resto = numero % 10**2
    
    #cociente = resto // 10**1
    #romano = romano + conversores[1][cociente]
    #resto = numero % 10**1
    
    #cociente = resto // 10**0
    #romano = romano + conversores[0][cociente]
    #resto = numero % 10**0

    
    for n in range(3,0-1,-1):
        cociente = numero // 10**n
        romano = romano + conversores[n][cociente]
        numero = numero % 10**n

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

