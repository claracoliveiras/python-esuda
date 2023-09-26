VETOR_UM = [2, 2]
VETOR_DOIS = [2, 2]

def produtoEscalar(VETOR_UM, VETOR_DOIS):
    resultado = 0;
    for i in range(len(VETOR_UM)):
        resultado += VETOR_UM[i] * VETOR_DOIS[i]
    
    return resultado

print(produtoEscalar(VETOR_UM, VETOR_DOIS))