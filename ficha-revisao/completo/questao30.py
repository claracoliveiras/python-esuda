VETOR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(VETOR)):
    if VETOR[i] % 2 == 0:
        VETOR[i] = None
        
j = 0
for i in range(len(VETOR)):
    if VETOR[i] != None:
        VETOR[j] = VETOR[i]
        j += 1
while j < len(VETOR):
    VETOR[j] = None
    j += 1
        
print(VETOR)