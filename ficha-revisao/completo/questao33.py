vetor = [1, 2, 2, 2, 3, 4]
numero = 2

def quantasVezes(vetor, numero):
    counter = 0
    for number in vetor:
        if number == numero:
            counter += 1
    
    return counter

print(quantasVezes(vetor, numero))