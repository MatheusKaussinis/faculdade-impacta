# A estrutura de repetição "For", é uma estrutura utilizada para que ocorra uma repetição para quando uma certa condição for verdadeira, ou seja, é um laço de repetição que fica repetindo suas instruções.
# Para que possamos verificar a contagem regressiva de 10 até 1, é preciso declarar o For, por conseguinte uma váriavel e utilizar da estrutura "in range()". "in range", segue a seguinte regra: (onde começo, onde termino, incremento dessa repetição).
#Neste caso queremos ir de 10 até 1, para que ocorra corretamente até que seja verdadeiro é preciso começar no 10, terminar no 0 (ele vai parar uma casa antes no 1), e colocar que deverá dimunir de -1 em -1, logo temos isso: 
for x in range(10, 0, -1):
    print(x)

# Estrutura de repetição "While", é um laço de repetição que irá repetir suas instruções enquanto sua condição for verdeira, o uso do laço "While", é válido quando não sabemos quantas vezes isso irá repetir, pode ser que ele se repita 1x ou 100x, não sabemos.
# Neste cado queremos ir de 10 até 1, então devemos fazer da seguinte forma, criamos uma váriavel que será o inicio da nossa repetição (10), declaramos o While, e fazemos uma condição que ele irá percorrer enquanto aquilo for verdadeiro, logo em seguida mandamos imprimir toda vez este número, e depois fazemos o descrécimo (-1), logo ele sempre irá atualizar a váriavel inicial por isso declaramos: variavelInicial = variavelInicial - 1, a cada fez que o laço ocorrer ele guarda o valor antigo da váriavel, faz a opração -1 e guarda um novo valor, assim indo do 10 até o 1, logo temos isso:
variavelInicial = 10
while variavelInicial:
    print(variavelInicial)
    variavelInicial = variavelInicial - 1

#função é um estrutura utilizada para minimizar uma possível repetiçã de código, caso você precise fazer 1 coisa mais de uma vez, é bom utilizar função, pois depois basta chamar ela. E caso queria fazer uma alteração nao precisa fazer essa alteração em mais de um lugar, e, sim apenas dentro da função, logo temos uma grande otimização perfomática do código.
def mediaSomaValores(parametro1, parametro2, parametro3): #Nesta linha ocorre a declaração da função, com o nome da função e os parâmetros que essa função espera, é primordial que sejam passados os parametros corretos, se pedir 3, e passar 4 dará erro ou se passar apenas 2 também dará erro, pois ela espera a passagem de 3 parêmetros
    media = (parametro1 + parametro2 + parametro3) / 4 #Aqui fazemos uma operação de média com os 3 parâmetros passado pela função
    soma = parametro1 + parametro2 #Aqui fazemos uma soma com apenas 2 parêmetros, por mais que foram passados 3, não necessariamente nas intruções precisará usar os três
    print(media) #Aqui temos uma forma de retornar o que essa função esta fazendo, por meio de um print, toda vez que essa função ser chamada, ela irá excutar suas intruções e irá imprimir o que desejamos.
    print(soma) #Aqui temos uma forma de retornar o que essa função esta fazendo, por meio de um print, toda vez que essa função ser chamada, ela irá excutar suas intruções e irá imprimir o que desejamos.
    
    return media, soma #Aqui temos a forma de retornar o valor, para utilizarmos fora da função, ou seja, pode ser que você não queira mostrar isso ao usuário com um print, mas sim apenas utilizar o valor retornado pela função em outro lugar do código.

mediaSomaValores(5, 4, 2) #Aqui estamos chamando a função mediaSomaValores e passando os valores necessários, neste caso 5(parametro1),4 (parametro2). 2(parametro3). Estes serão valores a serem utilizados dentro da função 
    


variavelNumeroInteiro = int(5) #A declaração de variável com o formato int, significa que a váriavel aceitará apenas NÚMEROS INTEIROS
variavelNumerosFloat = float(4.555555) #A declaração de variável com formato float, signigica que a váriavel aceitará números com ponto fluante, ou seja, NÚMEROS COM VÍRGULAS
variavelString = str('Olá, bora Ac05') #A declaração de variável com o formato str, significa que a váriavel aceitará apenas o formato de TEXTO, esse por sua vez sempre deve aparecer entre " " ou ' '

