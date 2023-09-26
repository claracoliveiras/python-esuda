VETOR = [1, 2, 3, 4, 5]
REMOVERNUMERO = 6


def acharNumero(VETOR, REMOVERNUMERO):
    for x in range(len(VETOR)):
        if VETOR[x] == REMOVERNUMERO:
            return True
    return False

def removerVetor(VETOR, REMOVERNUMERO):
    i = 0
    excluiu = False
    if acharNumero(VETOR, REMOVERNUMERO):
        while i < len(VETOR):
            if VETOR[i] == REMOVERNUMERO:
                VETOR[i] = VETOR[i + 1]
                excluiu = True
            elif excluiu and i < (len(VETOR) - 1):
                VETOR[i] = VETOR[i + 1]
            elif i == (len(VETOR) - 1):
                VETOR[i] = None

            i += 1
        return VETOR
    return "Erro"
        

print(removerVetor(VETOR, REMOVERNUMERO))