VETOR = []
querAdicionar = True

while querAdicionar == True:
    entradas = int(input("Adicione seus valores: "))
    VETOR += [entradas]
    querAdicionarConfirma = int(input("Digite 0 se quiser adicionar mais um numero e 1 se quiser sair do programa: "))
    if querAdicionarConfirma == 1:
        querAdicionar = False

print(VETOR)