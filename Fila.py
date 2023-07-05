class Fila:
    def __init__(self):
        self.fila_carros = []
        self.fila_drones = []

    def adicionar_carro(self, carro):
        self.fila_carros.append(carro)

    def adicionar_drone(self, drone):
        self.fila_drones.append(drone)

    def remover_carro(self):
        if self.fila_carros:
            return self.fila_carros.pop(0)
        else:
            print("A Fila de carros está vazia.")

    def remover_drone(self):
        if self.fila_drones:
            return self.fila_drones.pop(0)
        else:
            print("A Fila de drones está vazia.")

    def imprimir_fila_carros(self):
        if self.fila_carros:
            print("Fila de Carros:")
            for carro in self.fila_carros:
                carro.imprimir_dados()
        else:
            print("A Fila de carros está vazia.")

    def imprimir_fila_drones(self):
        if self.fila_drones:
            print("Fila de Drones:")
            for drone in self.fila_drones:
                drone.imprimir_dados()
        else:
            print("A Fila de drones está vazia.")
