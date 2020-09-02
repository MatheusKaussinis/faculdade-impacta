resposta = str(input())

if resposta == 'n':
    print('zero')
else:
    soma = quant = media = maior_velocidade = 0
    while resposta != 'n':
        ano = int(input('Digite o Ano do seu carro: '))
        velocidade = float(input('Digite a velocidade do seu carro: '))

        soma += velocidade
        quant += 1

        if quant == 1:
            maior_velocidade = velocidade
        else:
            if velocidade > maior_velocidade:
                maior_velocidade = velocidade
                
        resposta = str(input())
    media = soma / quant
    print('{:.2f}'.format(maior_velocidade))
    print('{:.2f}'.format(media))

