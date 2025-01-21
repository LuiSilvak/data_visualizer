# Visualizador de Dados com Matplotlib

import matplotlib.pyplot as plt

class VisualizadorDados:
    def __init__(self, dados, labels):
        self.dados = dados
        self.labels = labels

    def plotar_grafico_barras(self):
        """Plota um gráfico de barras com os dados fornecidos."""
        plt.bar(self.labels, self.dados)
        plt.xlabel('Categorias')
        plt.ylabel('Valores')
        plt.title('Gráfico de Barras - Visualizador de Dados')
        plt.show()

    def plotar_grafico_linhas(self):
        """Plota um gráfico de linhas com os dados fornecidos."""
        plt.plot(self.labels, self.dados, marker='o')
        plt.xlabel('Categorias')
        plt.ylabel('Valores')
        plt.title('Gráfico de Linhas - Visualizador de Dados')
        plt.show()

def main():
    # Dados de exemplo: Categroias e seus respectivos valores
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [12, 9, 15, 7, 20]

    # Criação da instância do visualizador de dados
    visualizador = VisualizadorDados(valores, categorias)

    # Exibição dos gráficos
    print("Escolha o tipo de gráfico que deseja visualizar: ")
    print("1 - Gráfico de Barras")
    print("2 - Gráfico de Linhas")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        visualizador.plotar_grafico_barras()
    elif opcao == "2":
        visualizador.plotar_grafico_linhas()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

        