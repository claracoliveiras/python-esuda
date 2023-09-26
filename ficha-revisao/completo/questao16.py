numero = int(input("Insira um numero: "))

def primo(numero):
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return "numero primo"
    else:
        if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
            return "o numero eh primo"
        else:
            return "o numero nao eh primo"

print(primo(numero))