VETOR = [1, 2, 3, 4]
VALOR = 4

def acharNumero(VETOR, REMOVERNUMERO):
    for x in range(len(VETOR)):
        if VETOR[x] == REMOVERNUMERO:
            return "Valor encontrado"
    return "Valor nao encontrado"

print(acharNumero(VETOR, VALOR))