#### Vinicius Cavalcanti - RA: 1902667 ####
def acharDenominador(numero):
    numeradorCima = 1
    adiciona = 1
    somatoria = 0

    for x in range(numero):
        numeroBaixo = (adiciona * adiciona)
        adiciona = adiciona + 1
        conta = numeradorCima / numeroBaixo
        somatoria = somatoria + conta
    print('{:.6f}'.format(somatoria))

numero = int(input())
acharDenominador(numero)
