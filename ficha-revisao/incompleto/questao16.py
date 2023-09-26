numero = int(input("Insira um numero: "))

def primo(numero):
    if numero == 1:
        return "Nao eh primo"
    if numero == 2:
        return "Primo"
    if numero != 2 and numero % 2 == 0 and numero % 3 == 0:
        return "Nao eh primo"
    if numero % numero == 0 and numero % 2 >= 0 :
        return "Primo"

print(primo(numero)) 