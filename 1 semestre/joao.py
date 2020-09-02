caracte = str(input())
if caracte == 'n':
    print("zero")
else:
    soma = quant = media = maior_velocidade = maior_ano = 0

    while caracte != 'n':
        ano = int(input())
        velocidade = float(input())

        soma += velocidade
        quant += 1 

        if quant == 1:
            maior_velocidade = velocidade
            maior_ano = ano
        else:
            if velocidade > maior_velocidade:
                maior_velocidade = velocidade
            if ano > maior_ano:
                maior_ano = ano

        caracte = str(input())
    media = soma / quant
    print('{:.2f}'.format(maior_velocidade))
    print(maior_ano)
    print('{:.2f}'.format(media))



