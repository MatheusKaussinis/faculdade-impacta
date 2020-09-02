# Linguagem de Programação II
# AC01 ADS-EaD - Números Especiais
#
# Email Impacta: matheus.kaussinis@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    count = 0 
    for i in range (1, n + 1): 
        if n % i == 0: 
            count += 1 
    if count != 2: 
        print ('False')
    else: 
        print ('True')

n = int(input('Digite um numero: '))
eh_primo(n)

pass

def lista_de_primos(n): 
    lista = []
    for i in range (1, n):
        count = 0 
        for x in range (1, i + 1):
            if i % x == 0:  
                count += 1
        if count <= 2: 
            lista.append(i)
    print(lista)
n = int(input('Digite um numero: '))
lista_de_primos(n)

pass

def eh_armstrong(n):
    numero_n = n
    quant_digito = len(str(n))
    soma_digitos = 0
    while n > 0:
        ult_digito = (n % 10) ** quant_digito
        soma_digitos += ult_digito
        n = n // 10
    if numero_n == soma_digitos:
        print('True')
    else:
        print('False')
n = int(input('Digite um numero: '))
eh_armstrong(n)

pass

def lista_armstrong(n):

    lista_armstrong = []
    for i in range(1 ,n + 1):
        soma_digitos = 0
        quant_digito = len(str(i))
        n = i
        while n > 0:
            digito = (n % 10) ** quant_digito
            soma_digitos += digito
            n //= 10
        if i == soma_digitos:
            lista_armstrong.append(i)
    print(lista_armstrong)

n = int(input('Digite um numero: '))
lista_armstrong(n)

pass

def eh_perfeito(n):
    count = 0
    for i in range (1, n): 
        if n % i == 0:
            count += i 
    if count == n:
        print('true')
    else:
        print('false')

n = int(input('Digite um numero : '))
eh_perfeito(n)

pass

def lista_de_perfeitos(n):
    lista = []
    for x in range(1, n):
        count = 0 
        for i in range (1, x): 
            if x % i == 0: 
                count += i 
        if count == x:
            lista.append(x)
    print(lista)       

n = int(input('Digite um numero : '))
lista_de_perfeitos(n)  

pass