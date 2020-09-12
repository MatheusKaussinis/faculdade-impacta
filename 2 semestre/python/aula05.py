class VeiculoAutomotivo():

    # __init__ função está obrigando que a class receba algum valor em seu parâmetro quanto for chamada externamente
    def __init__(self, Cilindradas):
        self.__Motorizacao = Cilindradas

    @property
    def Motorizacao(self):
        # __ significa que esse atributo só poderá ser recuperado dentro dessa class e em mais nenhum outro lugar extermp
        return self.__Motorizacao

    @Motorizacao.setter
    def Motorizacao(self, value):
        self.__Motorizacao = value

    def Ligar(self):
        return True

    def Buzinar(self, vezes):  # toda função dentro de uma class é preciso receber o seld como parâmetro para que a função possa receber tudo aquilo que está na class
        print(vezes)

        return


fusca = VeiculoAutomotivo(4)
fusca.Ligar()
fusca.Buzinar(3)

fusca.Motorizacao = 2000
print(fusca.Motorizacao)
