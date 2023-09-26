VETOR_INTEIRO = [1, 2, 3, 4]
VETOR_PARES = []

for i in range(len(VETOR_INTEIRO)):
    if VETOR_INTEIRO[i] % 2 == 0:
        VETOR_PARES += [VETOR_INTEIRO[i]]

print(VETOR_PARES)