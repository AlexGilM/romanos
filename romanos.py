class Romano:

    # ¿cómo creo un número romano?
    # con un "constructor"
    def __init__(self, entrada):
        print('Constructor con', entrada)
        if type(entrada) == int:
            self.valor = entrada
        elif type(entrada) == str:
            self.cadena = entrada
        else:
            raise TypeError('Solo acepto enteros o cadenas')
    
    def convertir_a_romano(self):
        print('Convertir a romano', self.valor)
        #validaciones
        if type(self.valor) != int:
            return f'Error:  {self.valor}  no es un entero'
        elif self.valor <= 0 or self.valor >=4000:
            return f'Error: {self.valor} fuera de rango 0> # <4000'   
        
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
        numero = self.valor

   

        
        for n in range(3,-1,-1):
            cociente = numero // 10**n
            romano = romano + conversores[n][cociente]
            numero = numero % 10**n

        #devolvemos resultado
        return romano

        def romano_a_entero(self):
            print('Romano a entero', self.valor_de_entrada)

