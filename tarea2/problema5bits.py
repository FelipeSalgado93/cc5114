import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19)
REAL_ARRAY = np.random.randint(2, size=5)

def generate_pool(N, size):
    N_array = list()
    for n in range(N):
        N_array.append(np.random.randint(2, size=size))
    print(N_array)
    return N_array

def evaluate(pool):
    for p in pool:
        if fitness(p) == len(REAL_ARRAY):
            return True
    return False

def fitness(ar):
    s = 0
    assert len(ar) == len(REAL_ARRAY)
    for x in range(len(ar)):
        if ar[x] == REAL_ARRAY[x]:
            s += 1
    return s

def best_fitness(pool):
    best = 0
    for p in pool:
        s = 0
        for x in range(len(p)):
            if p[x] == REAL_ARRAY[x]:
                s += 1
        if s > best:
            best = s
    return best

def tournement(N_array, k):
    best = None
    for i in range(k):
        candidate = N_array[np.random.randint(len(N_array))]
        if (best is None) or (fitness(candidate) > fitness(best)):
            best = candidate
    return best

def reproduction(p1, p2, m_rate):
    child = list()
    mix_pivote = np.random.randint(len(p1))
    for n in range(len(p1)):
        if n < mix_pivote:
            child.append(p1[n])
        else:
            child.append(p2[n])

        ran = np.random.rand()
        if ran < m_rate:
            if child[n] == 0:
                child[n] = 1
            else:
                child[n] = 0
    return child


len_real_pool = len(REAL_ARRAY)
len_base_pool = 5
k = 4
mix_rate = 0.05
generaciones = 0
bf = list()
generation_list = list()

base_pool = generate_pool(len_base_pool, len_real_pool)
bool = evaluate(base_pool)
generation_list.append(generaciones)
bf.append(best_fitness(base_pool))
while not bool:
    generaciones += 1
    if generaciones == 1000:
        break
    print('generacion ' + str(generaciones))
    parent_pool = list()
    for j in range(len_base_pool*2):
        parent_pool.append(tournement(base_pool, k))
    for i in range(len_base_pool):
        base_pool[i] = reproduction(parent_pool[2*i], parent_pool[2*i+1], mix_rate)
    generation_list.append(generaciones)
    bf.append(best_fitness(base_pool))
    bool = evaluate(base_pool)


fig, ax = plt.subplots()
ax.plot(generation_list, bf, color='r')
ax.set_xlabel("Generations")
ax.set_ylabel('Fitness (best)')

plt.title("Gen vs Fit")
fig.savefig("5bits.png")
plt.show()

