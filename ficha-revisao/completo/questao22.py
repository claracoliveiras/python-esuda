numero = int(input("Insira um numero: "))

def primo(numero):
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return True
    else:
        if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
            return True
        else:
            return False

def primoAnterior(numero):
    flag = False
    i = 1
    numAnterior = 0
    while not flag:
        if primo(numero - i):
            flag = True
            numAnterior = numero - i
        else:
            i += 1
    return numAnterior

def primoPosterior(numero):
    flag = False
    i = 1
    numPosterior = 0
    while not flag:
        if primo(numero + i):
            flag = True
            numPosterior = numero + i
        else:
            i += 1
    return numPosterior

print(f"O primo anterior a {numero} é {primoAnterior(numero)} e o posterior é {primoPosterior(numero)}")