class Carro():

    def __init__(self, marca, modelo, ano):
        """Inicializa os atributos que descrevem o carro"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = 0

    def descricao_veiculo(self):
        """Devolve dados do carro"""
        descricao = self.marca + ' - ' + self.modelo + ' - ' + str(self.ano)
        return descricao.title()

    def ler_odometro(self):
        """Exibe uma frase que mostra a quilometragem do carro"""
        print(f"A quilometragem do carro é {self.quilometragem}")

    def atualiza_quilometragem(self, km):
        """Define o valor da leitura do adometro com o valor especificado
        Rejeita a alteração se for valor menor para o hodometro"""
        if km >= self.quilometragem:
            self.quilometragem = km
        else:
            print("Você não pode baixar a quilometragem!")

    def pega_quilometragem(self, km):
        self.quilometragem += km


class Bateria():
    # modelando bateria para carro eletrico
    def __init__(self, tamanho_bateria=100):
        self.tamanho_bateria = tamanho_bateria

    def descricao_bateria(self):
        # Exibe uma frase que descreve a capacidade da bateria
        print(f"A capacidade da bateria é de {self.tamanho_bateria}-kwh")

    def alcance_bateria(self):
        # Exibe a frase sobre a distancia que o carro é capaz de percorrer com essa bateria
        if self.tamanho_bateria == 70:
            alcance = (3 * self.tamanho_bateria)
        elif self.tamanho_bateria == 80:
            alcance = (3 * self.tamanho_bateria)
        else:
            alcance = (3 * self.tamanho_bateria)

        print(
            f"Esse carro pode ir aproximadamente {alcance} quilometros com a carga completa")

    def atualiza_bateria(self):
        if self.tamanho_bateria != 85:
            self.tamanho_bateria = 85
            print(
                f"A bateria vai ser trocada pela correta de {self.tamanho_bateria}-kwh")
        else:
            print("A bateria esta correta")


class CarroEletrico(Carro):
    # Representa aspectos especificos do carro eletrico
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.bateria = Bateria()


carro_1 = Carro('ford', 'focus', 2014)
print(carro_1.descricao_veiculo())
carro_1.ler_odometro()
# carro_1.atualiza_quilometragem(12)
carro_1.atualiza_quilometragem(24)
carro_1.pega_quilometragem(24)
carro_1.ler_odometro()

carro_2 = CarroEletrico('tesla', 'model s', 2020)
print(carro_2.descricao_veiculo())
carro_2.bateria.descricao_bateria()
carro_2.bateria.alcance_bateria()
carro_2.bateria.atualiza_bateria()
