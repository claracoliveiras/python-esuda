palavra = "arara"

def palindromo(palavra):
    i = 0
    j = len(palavra) - 1
    while i != len(palavra):
        if palavra[i] == palavra[j]:
            i += 1
            j -= 1
        else:
            return "Não é um palíndromo"
    return "É um palíndromo"

print(palindromo(palavra))