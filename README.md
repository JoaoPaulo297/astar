# 🧭 Algoritmo A* para Resolução de Labirintos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Artificial Intelligence](https://img.shields.io/badge/IA-Busca_Heurística-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Este repositório contém a implementação do **Algoritmo de Busca A* (A-Star)** aplicado à resolução de labirintos em matrizes bidimensionais. O projeto aborda o problema sob a ótica da Inteligência Artificial, formalizando o labirinto como um espaço de estados e encontrando o caminho ótimo entre uma origem e um destino informados.

---

## 📝 Descrição do Problema

O labirinto é modelado como uma grade (matriz) de dimensões configuráveis, onde cada célula assume um estado específico:
* **Células Livres (1):** Caminhos válidos que o agente pode percorrer.
* **Obstáculos (0):** Paredes ou bloqueios intransitáveis.

O objetivo do agente é partir de um par ordenado de origem $(X_0, Y_0)$ e alcançar o estado objetivo $(X_d, Y_d)$ realizando o menor número de movimentos possíveis, computando deslocamentos verticais, horizontais e diagonais.

---

## 🧮 Funcionamento do Algoritmo A*

O algoritmo seleciona o próximo estado a ser explorado minimizando a função de custo total:

$$f(n) = g(n) + h(n)$$

Onde:
* **$g(n)$ (Custo Real):** O custo acumulado do caminho percorrido desde a célula de origem até a célula atual $n$.
* **$h(n)$ (Heurística):** A estimativa do custo restante para ir da célula atual $n$ até o destino final. No projeto, utiliza-se a **Distância Euclidiana** como função heurística admissível e consistente.

### 📋 Estrutura de Dados e Fluxo
* **Open List (Lista Aberta):** Implementada como uma fila de prioridade (*Min-Heap* usando a biblioteca `heapq` do Python) para garantir a extração eficiente do nó com o menor valor de $f(n)$.
* **Closed List (Lista Fechada):** Uma matriz booleana estática utilizada para registrar os estados já visitados, otimizando o tempo de execução e evitando loops redundantes.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Biblioteca Nativa:** `heapq` (para gerenciamento da Fila de Prioridade)
* **Estruturação Teórica:** Referências de Busca Heurística em Inteligência Artificial

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina. Siga os passos abaixo no terminal:

```bash
# 1. Clone o repositório
git clone [https://github.com/JoaoPaulo297/astar.git](https://github.com/JoaoPaulo297/astar.git)

# 2. Navegue até a pasta de código-fonte
cd astar/src

# 3. Execute o script principal
python Astar.py

