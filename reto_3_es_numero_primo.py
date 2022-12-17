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
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0: # dividiendo por los primeros
        return False
    else:
        return True # en caso que no cumpla ninguna de las anteriores

def run_primo():
    num = input("inserte un numero entero positivo: ") # se le pide el nuemro al usuario
    if num.isdigit(): # comprobamos que inserto un numero
        print(es_primo(numero = int(num))) # si es un numero comprobamos si es primo
        # y parseamos a int toda la entrada por teclado es considerada str
    else:
        print("\nSolo se admiten Numeros Enteros Positivos. Intentelo Nuevamente\n") # numero incorrecto
        run_primo() # relanzamos el programa

def cien_primeros_primos():
    primos = []
    valor = 0
    while len(primos) != 100:
        match valor:            
            case 2:
                primos.append(valor)
            case 3:
                primos.append(valor)
            case 5:
                primos.append(valor)
            case _:
                if es_primo(numero = valor):
                    primos.append(valor)
        valor += 1
    return primos       


if __name__ == '__main__':
    run_primo()    
    print(f"\nLos 100 primeros números primos son:\n{cien_primeros_primos()}\n")
    
        