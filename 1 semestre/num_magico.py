def numero_magico(a):
    numero_magico = 4
    if a // 1 == a:
        if a == numero_magico:
            print('numero magico')
        elif a == numero_magico / 2:
            print('muito menor')
        elif a == numero_magico * 2:
            print('muito maior')
        elif a < numero_magico:
            print('menor')
        elif a > numero_magico:
            print('maior')
       
    else:
        print('não é valido')

numero = float(input())
numero_magico(numero)