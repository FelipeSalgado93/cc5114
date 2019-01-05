import numpy as np
import matplotlib.pyplot as plt
from src import AST

np.random.seed(39)


def generar_arboles(N, altura):
    arboles = list()
    for n in range(N):
        arbol = ast.crearArbol(altura)
        arboles.append(arbol)
    return arboles


def evaluate(arboles):
    for arbol in arboles:
        if fitness(arbol) == 20:
            print(ast.imprimirArbol(arbol))
            return True
    return False

def funcion(x):
    return x**3 - 7*x**2 + 32

def fitness(arbol):# more is better
    score = 0
    for v in range(var*-1, var):
        real = funcion(v)
        var_arbol = ast.eval(arbol, v)
        if real - offset < var_arbol < real + offset:
            score += 1
    return score


def best_fitness(arboles):
    best = 0
    for a in arboles:
        s = fitness(a)
        if s > best:
            best = s
    return best


def tournament(arboles, k):
    best = None
    for i in range(k):
        candidate = arboles[np.random.randint(len(arboles))]
        if (best is None) or (fitness(candidate) > fitness(best)):
            best = candidate
    return best


def reproduction(arbol1, arbol2, m_rate):
    rdm = np.random.rand()
    if arbol1.izq is None:
        return arbol1
    else:
        if rdm < m_rate:
            arbol1.reemplazar(arbol2)
            return arbol1
        else:
            rdm2 = np.random.rand()
            if rdm2 < 0.25:
                arbol1.izq.reemplazar(arbol2.izq)
            elif 0.25 <= rdm2 < 0.5:
                arbol1.izq.reemplazar(arbol2.der)
            elif 0.5 <= rdm2 < 0.75:
                arbol1.der.reemplazar(arbol2.izq)
            else:
                arbol1.der.reemplazar(arbol2.der)
        return arbol1

#   INICIALIZACION
ast = AST.ast
AST.altura = 2
altura = AST.altura
offset = 10
var = 10
num_arboles = 30
k = 20
mix_rate = 0.7
MAX_GEN = 200


generaciones = 0
bf = list()
generation_list = list()

arboles = generar_arboles(num_arboles, altura)
#print(ast.imprimirArbol(arboles[0]))
#print(ast.imprimirArbol(arboles[1]))
#print(ast.imprimirArbol(reproduction(arboles[0], arboles[1], mix_rate)))


bool1 = evaluate(arboles)


# listas para plotear
generation_list.append(generaciones)
bf.append(best_fitness(arboles))
while not bool1:
    generaciones += 1
    if generaciones == MAX_GEN:
        break
    print('generacion ' + str(generaciones))
    parent_pool = list()
    for j in range(num_arboles*2):
        parent_pool.append(tournament(arboles, k))
    for i in range(num_arboles):
        arboles[i] = reproduction(parent_pool[2*i], parent_pool[2*i+1], mix_rate)
    generation_list.append(generaciones)
    bf.append(best_fitness(arboles))
    bool1 = evaluate(arboles)


# Script para plotear
fig, ax = plt.subplots()
ax.plot(generation_list, bf, color='r')
ax.set_xlabel("Generations")
ax.set_ylabel('Fitness (best)')

plt.title("Gen vs Fit")
fig.savefig("test1.png")
plt.show()
