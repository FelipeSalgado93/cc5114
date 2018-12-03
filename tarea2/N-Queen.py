import numpy as np
import matplotlib.pyplot as plt

np.random.seed(39)


def generate_boards(N, size):
    N_boards = list()
    for n in range(N):
        arr = np.arange(size)
        np.random.shuffle(arr)
        N_boards.append(arr)
    return N_boards


def evaluate(boards):
    for b in boards:
        if fitness(b) == 0:
            print(b)
            return True
    return False


def fitness(board):
    score = choques(board)  # less is better
    return score


def choques(board):
    largo = len(board)
    c = 0
    x = 0
    while x < largo:
        z = x + 1
        while z < largo:
            if board[x] == board[z]:
                c += 1
            elif abs(x - z) == abs(board[x] - board[z]):
                c += 1
            z += 1
        x += 1
    return c


def best_fitness(boards):
    best = MAX_SCORE
    for b in boards:
        s = fitness(b)
        if s < best:
            best = s
    return best


def tournament(boards, k):
    best = None
    for i in range(k):
        candidate = boards[np.random.randint(len(boards))]
        if (best is None) or (fitness(candidate) < fitness(best)):
            best = candidate
    return best


def reproduction(p1, p2, m_rate):
    child = list()
    largo_tab = len(p1)
    mix_pivote = np.random.randint(largo_tab)
    for n in range(largo_tab):
        if n < mix_pivote:
            child.append(p1[n])
        else:
            child.append(p2[n])

        ran = np.random.rand()
        if ran < m_rate:
            child[n] = np.random.randint(len(p1))
    return child


#   INICIALIZACION
len_board = 16
len_board_pool = 25
k = 20
mix_rate = 0.05
MAX_GEN = 200

MAX_SCORE = sum(range(len_board))


generaciones = 0
bf = list()
generation_list = list()

board_pool = generate_boards(len_board_pool, len_board)
bool1 = evaluate(board_pool)


# listas para plotear
generation_list.append(generaciones)
bf.append(best_fitness(board_pool))
while not bool1:
    generaciones += 1
    if generaciones == MAX_GEN:
        break
    print('generacion ' + str(generaciones))
    parent_pool = list()
    for j in range(len_board_pool*2):
        parent_pool.append(tournament(board_pool, k))
    for i in range(len_board_pool):
        board_pool[i] = reproduction(parent_pool[2*i], parent_pool[2*i+1], mix_rate)
    generation_list.append(generaciones)
    bf.append(best_fitness(board_pool))
    bool1 = evaluate(board_pool)


# Script para plotear
fig, ax = plt.subplots()
ax.plot(generation_list, bf, color='r')
ax.set_xlabel("Generations")
ax.set_ylabel('Fitness (best)')

plt.title("Gen vs Fit")
fig.savefig("test1.png")
plt.show()
