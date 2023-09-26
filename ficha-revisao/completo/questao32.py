vetor = ['arroz', 'feijao', 'batata']
palavra = 'arroz'

def encontrarPalavra(vetor, palavra):
    for palavraa in vetor:
        if palavraa == palavra:
            return True
    return False

print(encontrarPalavra(vetor, palavra))