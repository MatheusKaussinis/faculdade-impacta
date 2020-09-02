#TUPLA - Não pode ser modificada 
tupla = (1, 2, 3)

#LISTA - Pode ser modificada, append, remove, sort
lista = [1, 3, 4, 5]
lista.append(3) # como ficou = [1, 3, 4, 5, 3] adiciona um elemento
lista.remove(3) #remove um elemento
lista.pop(5)#apagar um elemento que está no indicie 5
lista.insert(1, 5) #insirir um novo elemento, na posição e depois qual é o elemento
lista.sort() #Coloca elementos em ordem
lista.index(5) #Saber a posição de um elemento
lista(enumere(lista)) #transforma a lista em sub tuplas dentro, com a posição e o elemento: [(0,1), (1,3), (2,4), (3,5)]
