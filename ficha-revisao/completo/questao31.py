VETOR = [3, 4, 2, 0]

def valorMinimo(VETOR):
    valorMin = VETOR[0]
    for i in range(len(VETOR)):
        if VETOR[i] < valorMin:
            valorMin = VETOR[i]
    return valorMin

print(valorMinimo(VETOR))