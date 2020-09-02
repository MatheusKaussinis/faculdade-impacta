######## #achar um número de indice que está lista
# exemplo_de_lista = [1,2,5,5,2,4,4,6,7,8,5]
# indice = 0
# for indice in range(0,len(exemplo_de_lista),2):
#     if exemplo_de_lista[indice] == 1:
#         print(indice)
#     indice += 1





### achar indice par####
# lista_par = [1,2,4,6,5,7,8,10,9,6]
# for indice_1 in range(0,len(lista_par),2):
#     print(lista_par[indice_1])





### achar indice impar
# lista_par = [1,2,4,6,5,7,8,10,9,6]
# for indice_1 in range(1,len(lista_par),2):
#     print(lista_par[indice_1])





####### achar os 5 primeiros itens de uma lista
# listar = [1,2,5,8,9,6,3,5,4]
# print(listar[0:5])

### Imprimir cada sublista
# lista = [[0, 1 , 2], [3, 4, 5], [6, 7, 8]]
# for i in range(0, len(lista)): 
#     for j in range(0, len(lista[i])):
#         print(lista[i][j])


### alterar elementos em posições especificas
# lista = [1,2,3,4,5,6]

# for i in range(0, len(lista)):## len(lista)está alterando todos os elementos de todos os indices ## for i in range(0, 5): aqui eu altero os elementos dos indices 0 até 5 pelo número 5
#     lista[i] = 0
# print(lista)


lista = [[0, 1 , 2], [3, 4, 5], [6, 7, 8]]
altera = lista[1]
altera[0] = 5
print(altera)

for item in range(1, len(var_lista)):
        print(item*7)
