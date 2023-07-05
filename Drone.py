from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtd_helices):
        super().__init__(marca, modelo)
        self._qtd_helices = qtd_helices

    def imprimir_dados(self):
        print(f"Drone: {self.marca} {self.modelo}, Quantidade de Hélices: {self._qtd_helices}")