import numpy as np


class Perceptron:

    def __init__(self, weight_list, bias, learning_rate=0.1):
        self.weight_list = np.array(weight_list)
        self.bias = bias
        self.learning_rate = learning_rate

    def training(self, train_list, real_value):
        result = self.eval(train_list)
        diff = real_value - result
        self.weight_list += np.array(train_list)* diff * self.learning_rate
        self.bias += self.learning_rate * diff

    def eval(self, train_list):
        assert len(self.weight_list) == len(train_list)
        suma = sum(self.weight_list * np.array(train_list))
        result = 0
        if suma + self.bias > 0:
            result = 1
        return result


class Sigmoid(Perceptron):
    output = None
    delta = None

    def __init__(self, weight_list, bias, learning_rate=0.5, threshold=0.5):
        super().__init__(weight_list, bias, learning_rate=learning_rate)
        self.threshold = threshold

    def training(self, train_list, real_value):
        result = self.eval(train_list)
        diff = real_value - result
        self.update_delta(diff)
        self.update_weights(np.array(train_list))
        self.update_bias()

    def eval(self, train_list):
        assert len(self.weight_list) == len(train_list)
        suma = sum(self.weight_list * np.array(train_list)) + self.bias
        total_res = 1. / (1. + np.exp(-suma))
        self.output = total_res
        return total_res

    def update_delta(self, error):
        self.delta = error * self.output * (1.0 - self.output)

    def update_weights(self, pesos):
        for i in range(len(pesos)):
            self.weight_list[i] += (self.learning_rate * self.delta * pesos[i])

    def update_bias(self):
        self.bias += (self.learning_rate * self.delta)
