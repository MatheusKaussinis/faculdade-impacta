numero_principal = int(input())
numero_limitante = int(input())

numeros_naturais = 1
ver = numero_principal

while ver < numero_limitante:
    if (ver == numero_limitante):
        break
    else:
        multiplica = numero_principal * numeros_naturais
        ver = multiplica
        numeros_naturais = numeros_naturais + 1
numeros_naturais = numeros_naturais - 2
print("O numero", numero_principal, "tem", numeros_naturais, "multiplos menores que", str(numero_limitante) + ".")