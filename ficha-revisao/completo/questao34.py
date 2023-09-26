vetor = [1, 2, 3, 4, 5, 6]

def recolocar(VETOR):
    valorMin = VETOR[0]
    for i in range(len(VETOR)):
        if VETOR[i] < valorMin:
            valorMin = VETOR[i]

    valorMax = VETOR[0]
    for i in range(len(VETOR)):
        if VETOR[i] > valorMax:
            valorMax = VETOR[i]
            
    numeroRepos = valorMax / valorMin
    for i in range(len(VETOR)):
        VETOR[i] = numeroRepos
    return VETOR

print(recolocar(vetor))