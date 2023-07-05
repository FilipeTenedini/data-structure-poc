from Carro import Carro
from Drone import Drone
from Fila import Fila

def main():
    fila = Fila()

    while True:
        print("\nMenu:")
        print("1. Adicionar Carro à Fila")
        print("2. Adicionar Drone à Fila")
        print("3. Remover Carro da Fila")
        print("4. Remover Drone da Fila")
        print("5. Imprimir Fila de Carros")
        print("6. Imprimir Fila de Drones")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            marca = input("Qual a marca do Carro: ")
            modelo = input("Qual o do Carro: ")
            portas = int(input("Qual a quantidade de portas do Carro: "))
            carro = Carro(marca, modelo, portas)
            fila.adicionar_carro(carro)
            print("Carro adicionado.")

        elif escolha == "2":
            marca = input("Qual a marca do Drone: ")
            modelo = input("Qual o do Drone: ")
            qtd_helices = int(input("Qual a quantidade de hélices do Drone: "))
            drone = Drone(marca, modelo, qtd_helices)
            fila.adicionar_drone(drone)
            print("Drone adicionado.")

        elif escolha == "3":
            carro_removido = fila.remover_carro()
            if carro_removido:
                print(f"Carro removido: {carro_removido.marca} {carro_removido.modelo}")

        elif escolha == "4":
            drone_removido = fila.remover_drone()
            if drone_removido:
                print(f"Drone removido: {drone_removido.marca} {drone_removido.modelo}")

        elif escolha == "5":
            fila.imprimir_fila_carros()

        elif escolha == "6":
            fila.imprimir_fila_drones()

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Escolha novamente.")


main()
