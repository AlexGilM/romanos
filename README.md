# romanos
creamos un conversor de numeros romanos a decimal y viceversa

## Primera parte: convertir de entero a romano
Crear una función que reciba como parametro de entrada un número entero
y devuelva una cadena que represente ese número como romano.

- Los romanos no tenían cero. (interpretación: cero == '')
- Debe aceptar números entre el 1 y el 3999 (ambos incluidos)

**¿Cómo lo abordamos?**
 - Definir los valores:
    - I === 1
    - V === 5
    - X === 10
    - L === 50
    - C === 100
    - D === 500
    - M === 1000
1. Crear una función
2. La función recibe un parámetro
3. Validar que la entrada reciba es un número entero
    3.1 tiene que ser mayor que cero
    3.2 Tiene que ser menor que 4000
4. Devuelve una cadena
'''
1137 ==> 'MCXXXV'
||||_________ VII ..... 7 Unidades = 7 * 10^0
|||__________ XXX ..... 3 Decenas = 3 * 10^1
||___________ C ....... 1 Centenas = 1 * 10^2
|____________ M ....... 1 Millares = 1 * 10^3
Mirar si tiene miles.... al ser mil y "pico" ponemos una M

1137 = 1 * 10^3 + 1 * 10^2 + 3 * 10^1 + 7 * 10^0

1137/1000 = 1.137 -----> solo utilizamos la parte entera
1137 // 1000 = 1 (la // me devuelve el cociente) covierto el 1 en una M
2137 // 1000 = 2 convierto el 2 en MM
3137 // 1000 = 3 convierto el 3 en MMM
4... nos da error
'''

## Seguna parte: convertir de romano a entero

## Referencia de comandos GIT
- 'git remote': lista todos los espacios remotos a los que hace referencia el repositorio local (y, por tanto, puede sicronizar cambios en él)
- 'git remote get-url origin': 'origin' es el nombre del espacio remoto (en este caso Github) y con este comando podemos ver la URl a la que hace referencia. En el caso de este repo: https://github.com/KeepCodingCeroXXII/romanos.git
- 'git clone <url-del-repositorio>': hace una copia del repositorio remoto en la maquina local
- 'git clone <url-del-repositorio> <destino>': igual al anterior pero permite crear la copia en una carpeta con el nombre que especificamos en destino
- 'git log' : permite explorar el histórico de commits
- 'git log --oneline': simplifica la salida del log poniendo solamente el hash y el mensaje del commit

- 'git fetch': actualiza la información de las ramas y los commits disponibles en el repositorio remoto
- 'git pull': sincroniza desde el repositorio remoto hacia la maquina local el contenido de los commits de la rama actual.
- 'git push': sincroniza desde la maquina local hacia el repositorio el contenido de los commits de la rama actual.
'