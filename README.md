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
## Seguna parte: convertir de romano a entero

## Referencia de comandos GIT
- 'git remote': lista todos los espacios remotos a los que hace referencia el repositorio local (y, por tanto, puede sicronizar cambios en él)
- 'git remote get-url origin': 'origin' es el nombre del espacio remoto (en este caso Github) y con este comando podemos ver la URl a la que hace referencia. En el caso de este repo: https://github.com/KeepCodingCeroXXII/romanos.git