def es_primo(numero:int)->bool:
    """
    Dice si un nuemro es primo o no

    Atributos:
     - nuemro : int

    Return:
     - bool
    """
    if numero < 2: # el 2 es primer numero primo por lo tanto los menores que el no son primos
        # para este caso solo se evaluan los positivos
        return False
    elif numero == 2 or numero == 3 or numero == 5: # son los primos
        return True
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0: # dividiendo por los primeros primos
        return False
    else:
        return True # en caso que no cumpla ninguna de las anteriores

def run_primo():
    """
    Logica de ejecucion del programa

    Atributos:
     - None
    
    Return:
     - None
    """
    num = input("inserte un numero entero positivo: ") # se le pide el nuemro al usuario
    if num.isdigit(): # comprobamos que inserto un numero
        print(es_primo(numero = int(num))) # si es un numero comprobamos si es primo
        # y parseamos a int toda la entrada por teclado es considerada str
    else:
        print("\nSolo se admiten Numeros Enteros Positivos. Intentelo Nuevamente\n") # numero incorrecto
        run_primo() # relanzamos el programa

def cien_primeros_primos()->list:
    """
    Muestra cuales son los primeros 100 numeros primos

    Atributos:
     - None
    
    Return:
     - primos : list
    """
    primos = []# lista vacia para guardar los numeros primos
    valor = 0 # variable por la cual vamos comprobando los numeros
    while len(primos) != 100: # ciclo para comprobar si ya tenemos los 100 primos
        match valor: # usamos un match case para comprobar el valor de los numeros mas limpio el codigo          
            case 2: # si el numero es 2 lo agregamos lo mismo pasa con 3 y 5
                primos.append(valor)
            case 3:
                primos.append(valor)
            case 5:
                primos.append(valor)
            case _: # en caso que no cumpla los criterios anteriores comprobamos si es primo y si lo es lo añadimos
                if es_primo(numero = valor):
                    primos.append(valor)
        valor += 1 # incrementamos el valor de los numeros en 1
    return primos # retornamos la lista de los 100 primos      


if __name__ == '__main__':
    run_primo()    
    print(f"\nLos 100 primeros números primos son:\n{cien_primeros_primos()}\n")
    
        