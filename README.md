# Reto-01---POO
Desarrollo de los ejericios del reto 01:\

Pd: Cabe recalcar que el desarrollo de la asignatura "Programación para computadores" la vi toda en Python, por ende tengo buenas bases y conocimientos respecto a este lenguaje. Esto justificando el uso de algunas funciones dentro del desarrollo de mis ejercicios.\
  
1. Cree una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función serán los dos operandos y el carácter usado para la operación. entrada: (1,2,"+") , salida (3).  

En el desarrollo de este ejercicio simplemente se plantean las variables, dos que reciban solo enteros y una que reciba una cadena de texto; esta última esta condicionada a cadenas especificas que permiten calcular el resultado correspondiente y retornarlo.  

```python
def Calculator(a: int, b: int, operation: str):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return False, print("No se puede dividir entre 0")
        else:
            return a / b
    else:
        return False, print("Operación inválida")

print(Calculator(2, 3, "+"))
print(Calculator(4, 7, "-"))
print(Calculator(2, 6, "*"))
print(Calculator(3, 0, "/"))
print(Calculator(8, 4, "/"))
print(Calculator(0, 7, "^"))
```

2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.  

Para este ejercicio, se estable la variable que permite el ingreso de la palabra a validar y mediante un ciclo se ingresa cada letra de dicha palabra en una lista, luego de igual manera se ingresan nuevamente las letras pero en orden contrario (De la última a la primera) en una nueva lista; y al final se comparan estas dos listas para validar si cumple la condición de ser palíndroma o no.  

```python
word: str = input()

def Palindromo(word: str):
    letters = list()
    for letter in word:
        letters.append(letter)
    new_word = list()
    for letter in range(len(letters)-1, -1, -1):
        new_word.append(letters[letter])
    if new_word == letters:
        return True
    else:
        return False

print(Palindromo(word))
```

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.  

En este caso, se reciben los números y se guardan en una lista, luego se ingresa a un ciclo que recorre número por número, allí se verifica primero que sea mayor a 1, pues no se reciben negativos, luego se verifica si el número es divisible por algún número diferente a 1 o sí mismo, si es así no sería primo y se vería reflejado en una variable booleana establecida al inicio del ciclo. Al finalizar se compara dica variable y si el número es primo (True), se agrega a la lista vacia previamente creada y que sera impresa para mostrar el resultado final.  
Nota: Las funciones de .split() detecta los espacios para separar cada componente de la lista a generar; map() permite recibir los elementos para devolverselos o retornarlos a la lista con la funcion list(); y por último, la función "".join() une los elementos de la lista y deja un espacio entre ellos.   

```python
def Prime_Num():
    num_list = list(map(int, input("Ingrese números separados por espacios: ").split()))
    prime_list = []
    for num in num_list:
        prime = False
        if num > 1:
            prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(num)
    print(" ".join(map(str, prime_list)))

print(Prime_Num())
```

4. Escribir una función que reciba una lista de números enteros y devolver la mayor suma entre dos elementos consecutivos.  

Al igual que el anterior, primero se reciben los números y se almacenan en una lista, luego se hace una pequeña comprobación de que sean más de dos elementos para que haya una lógica de comparación; y mediante un ciclo que recorre los numeros del 1 al penúltimo valor de la lista para que se recorra en parejas se suman los números de dichas parejas y se compara este valor con el valor anterior, almacenado en una variable previamente creada en 0; para siempre guardar el mayor resultado. Y al final se muestra este resultado final.  

```python
def Sum_Par():
    list_num = list(map(int, input("Ingrese números: ").split()))
    result = 0
    if len(list_num) < 2:
        return False
    for i in range(len(list_num) - 1):
        current_sum = list_num[i] + list_num[i + 1]
        if current_sum > result:
            result = current_sum
    return result

print(Sum_Par())
```

5. Escribir una función que reciba una lista de cadenas y retorne únicamente aquellos elementos que tengan los mismos caracteres. por ejemplo entrada: ["amor", "roma", "perro"], salida["amor", "roma"]

Aquí se reciben las palabras y se reservan dentro de una lista, se genera una lista vacia donde ira los resultados. Luego mediante un ciclo se recorre cada palabra y en la variable base se guarda la lista ordenada de cada letra de la primera palabra para realizar la comparación, luego se recorre cada palabra para compararla con la base y guardarla en una nueva lista de grupo si es anagrama; al finalizar ese ciclo y si la lista tiene más de un elemento se guarda el grupo de anagramas en la lista de resultado final; así mismo se repite el ciclo para comparar todas las palabras entre ellas e imprimir los grupos de anagramas que se encuentren.  

```python
def Anagrama():
    list_word = list(map(str, input("Ingrese palabras: ").split()))
    anagram = []
    for i in range(len(list_word)):
        base = sorted(list_word[i])
        grupo = []
        for palabra in list_word:
            if sorted(palabra) == base:
                grupo.append(palabra)
        if len(grupo) > 1 and grupo not in anagram:
            anagram.append(grupo)
    return anagram

print(Anagrama())
```
