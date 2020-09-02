def numero_magico(numero_inteiro):
    numero_magico = 6
    if numero_inteiro // 1 != numero_inteiro:
        print('nao valido')
    elif numero_inteiro == numero_magico:
        print('magico')
    elif numero_inteiro == numero_magico * 2 or numero_inteiro > numero_magico * 2:
        print('muito maior')
    elif numero_inteiro == numero_magico / 2 or numero_inteiro < numero_magico / 2:
        print('muito menor')
    elif numero_inteiro < numero_magico:
        print('menor')
    elif numero_inteiro > numero_magico:
        print('maior')
    
valor_inteiro = float(input())
numero_magico(valor_inteiro)