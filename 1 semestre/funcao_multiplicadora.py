def funcao_multiplicadora(var_lista):
    quantidade_lista = len(var_lista)
    if type(var_lista) == list:
       
        if quantidade_lista < 4:
            print(var_lista)
        else:
            tirar = var_lista.pop(0)
            tirar2 = var_lista.pop(1)
            var_lista = [i * 7 for i in var_lista]
            var_lista.insert(0, tirar)
            print(var_lista)
    else:
         print('[]')
lista = [1,1,1,1,1,1,1]
funcao_multiplicadora(lista)