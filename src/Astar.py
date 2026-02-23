import math
import heapq

# Definição da classe célula
class Cell:
    def __init__(self):
        self.parent_i = 0  # Índice de linha da célula pai
        self.parent_j = 0  # Índice de coluna da célula pai
        self.f = float('inf')  # Custo total da célula (g + h)
        self.g = float('inf')  # Custo do caminho da origem até essa célula
        self.h = 0  # Custo previsto pela heurística dessa célula até o destino


# Verifica se uma célula é válida
def is_valid(row, col, numROWS, numCOLS):
    return (row >= 0) and (row < numROWS) and (col >= 0) and (col < numCOLS)

# Verifica se uma célula está livre
def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Verifica se uma célula é o objetivo
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calcula o valor da heurística de uma célula (Distância euclidiana para o destino)
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5



# Traça o caminho encontrado da origem até o destino
def trace_path(cell_details, dest):
    path = []
    row = dest[0]
    col = dest[1]

    # Traça o caminho do destino até a origem usando os parâmetros da célula pai
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Adiciona a célula de origem para o caminho
    path.append((row, col))
    # Inverte o caminho para obter o trajeto da origem até o destino
    path.reverse()

    print("Número de passos: ", len(path)- 1)
    print("O caminho é: ")

    # Imprime o caminho
    for i in path:
        print("->", i, end=" ")
    print()


# Algoritmo A*
def a_star_search(grid, src, dest, numROWS, numCOLS):
     # Inicializa cada célula
    cell_details = [[Cell() for _ in range(numCOLS)] for _ in range(numROWS)]
    # Inicializa os parâmetros da célula de origem
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j
    # Inicializa a lista aberta (células a serem visitadas) com a célula de origem
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))
    # Inicializa a flag para saber se o destino foi encontrado
    found_dest = False
    # Inicializa a lista fechada (células já visitadas)
    closed_list = [[False for _ in range(numCOLS)] for _ in range(numROWS)]
    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Obtêm a célula com o menor valor f da lista aberta
        p = heapq.heappop(open_list)
        # Marca a célula como visitada
        i = p[1]
        j = p[2]
        closed_list[i][j] = True
        if is_destination(i, j, dest):
            print("A célula de destino foi encontrada")
            # Traça e imprime o caminho da origem até o destino
            trace_path(cell_details, dest)
            found_dest = True
            return
        
        # Para cada direção (incluindo as diagonais), verifique os sucessores
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            # Se o sucessor é válido, está livre e não foi visitado
            if is_valid(new_i, new_j, numROWS, numCOLS) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # Calcula os novos valores de f, g e h
                g_new = cell_details[i][j].g + 1.0
                h_new = calculate_h_value(new_i, new_j, dest)
                f_new = g_new + h_new
                # Se a célula não está na lista aberta ou o novo valor de f é menor
                if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                    # Adicione a célula para a lista aberta
                    heapq.heappush(open_list, (f_new, new_i, new_j))
                    # Atualiza os parâmetros da célula
                    cell_details[new_i][new_j].f = f_new
                    cell_details[new_i][new_j].g = g_new
                    cell_details[new_i][new_j].h = h_new
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
    # Se o objetivo não foi encontrado depois de visitar todas as células
    if not found_dest:
        print("Failed to find the destination cell")


# Função para interagir com o usuário
def user_interaction():

    largura = 120
    print("-" * largura)
    print("SEJA BEM-VINDO".center(largura))
    print("Esta é uma aplicação do Algoritmo A* para a resolução de problemas de labirinto".center(largura))
    print("-" * largura)

    print("Nesta aplicação, um labirinto é representado por uma matriz, onde 1 é CAMINHO LIVRE e 0 é BLOQUEIO.")
    print("Exemplo de labirinto: [\n[0, 1, 1],\n[1, 0, 0],\n[1, 1, 1]\n]")

    print("-" * largura)
    print("Obtenção dos dados do labirinto".center(largura))
    print("-" * largura)


    height = int(input(f"Qual a altura do labirinto: "))
    width = int(input(f"Qual o comprimento do labirinto: "))

    maze = []

    for i in range(height):
        entrada = input(f"Defina a linha {i+1} do labirinto com {width} elementos(apenas 0s e 1s) separados por espaços: ")
        linha = [int(x) for x in entrada.split()]
        
        while len(linha) != width:
            print("Número de elementos na linha do labirinto errado!")
            entrada = input(f"Defina a linha {i+1} do labirinto com {width} elementos(apenas 0s e 1s) separados por espaços novamente: ")
            linha = [int(x) for x in entrada.split()]
        
        while not all(x in [0, 1] for x in linha):
            print("Use apenas 0s e 1s!")
            entrada = input(f"Defina a linha {i+1} do labirinto com {width} elementos(apenas 0s e 1s) separados por espaços novamente: ")
            linha = [int(x) for x in entrada.split()]
          
        
        maze.append(linha)

    for i in range(1):

        entrada1 = input(f"Defina a célula de origem [formato: linha coluna]: ")
        src = [int(x) for x in entrada1.split()]

        while not is_valid(src[0], src[1], height, width) or not is_unblocked(maze, src[0], src[1]):
            print("Origem não válida")
            entrada1 = input(f"Defina a célula de origem novamente [formato: linha coluna]: ")
            src = [int(x) for x in entrada1.split()]

        entrada2 = input(f"Defina a célula de destino [formato: linha coluna]: ")
        dest = [int(x) for x in entrada2.split()]

        while not is_valid(dest[0], dest[1], height, width) or not is_unblocked(maze, dest[0], dest[1]):
            print("Destino não válido")
            entrada2 = input(f"Defina a célula de destino novamente [formato: linha coluna]: ")
            dest = [int(x) for x in entrada2.split()]

    
    print("-" * largura)
    print("Representação da matriz do labirinto: ", maze)

    print("-" * largura)
    print("Resultado".center(largura))
    print("-" * largura)

    

    a_star_search(maze, src, dest, height, width)


def main():
    
    user_interaction()

if __name__ == "__main__":
    main()