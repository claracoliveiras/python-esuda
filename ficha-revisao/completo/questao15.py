VETOR = [1, 2, 3, 4]

def soma_Vetor(VETOR):
    soma = 0;
    for i in range(len(VETOR)):
        soma += VETOR[i]
    return soma

print(soma_Vetor(VETOR))