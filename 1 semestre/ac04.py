#### Matheus Kaussinis da Silva - RA: 1902621 ####
def calcularDenominador(num):
    numEmbaixo = 1
    numEmcima = 1
    count = 1
    soma = 0
    contador = 3
    while count <= num:
        divisao = numEmcima / numEmbaixo
        numEmbaixo = numEmbaixo + contador
        soma += divisao
        count = count + 1
        contador = contador + 2
    print('{:.6f}'.format(soma))
numeroMaximo = int(input())
calcularDenominador(numeroMaximo)
