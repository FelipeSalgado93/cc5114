import random
import copy


class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def reemplazar(self, nodo):
        self.izq = nodo.izq
        self.der = nodo.der
        self.valor = nodo.valor

    def copiar(self):
        return copy.deepcopy(self)


class NodoInterno(Nodo):
    def __init__(self, valor, izq, der):
        super().__init__(valor, izq, der)


class NodoHoja(Nodo):
    def __init__(self, valor):
        super().__init__(valor)


class AST:
    def __init__(self, funciones, terminales, altura):
        self.funciones = funciones
        self.terminales = terminales
        self.altura = altura

    def crearArbol(self, max_altura=None):
        altura_actual = None
        if max_altura is not None:
            altura_actual = max_altura
        else:
            altura_actual = self.altura
        if altura_actual > 0:
            return NodoInterno(random.choice(self.funciones), self.crearArbol(altura_actual-1), self.crearArbol(altura_actual-1))
        else:
            return NodoHoja(random.choice([random.choice(self.terminales), "V"]))

    def imprimirArbol(self, arbol):
        s = ""
        if arbol.valor in terminales:
            return arbol.valor
        elif arbol.valor == "V":
            return "V"
        elif arbol.valor in self.funciones:
            s = "[" + arbol.valor + " " + str(self.imprimirArbol(arbol.izq)) + " " + str(self.imprimirArbol(arbol.der)) + "]"
            return s

    def eval(self, ast, var):
        if ast.valor in self.terminales:
            return ast.valor
        elif ast.valor == "V":
            return var
        elif ast.valor in self.funciones:
            if ast.valor == "x":
                return self.eval(ast.izq, var) * self.eval(ast.der, var)
            elif ast.valor == "+":
                return self.eval(ast.izq, var) + self.eval(ast.der, var)
            elif ast.valor == "-":
                return self.eval(ast.izq, var) - self.eval(ast.der, var)
            elif ast.valor == "max":
                return max(self.eval(ast.izq, var), self.eval(ast.der, var))


funciones = ["x", "+", "-", "max"]
terminales = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
altura = 5
ast = AST(funciones, terminales, altura)
#arbol = ast.crearArbol(3)
#print(ast.imprimirArbol(arbol))
#print(ast.eval(arbol, 10))
