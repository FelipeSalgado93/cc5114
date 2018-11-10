import random
import numpy as np
from Neurona import Sigmoid


class CapaNeurona:
    def __init__(self, number=None, learning_rate=0.5):
        self.number = number
        self.neuronas = list()
        self.learning_rate = learning_rate

    def __len__(self):
        return len(self.neuronas)

    def initialize(self, n_inputs=None, weights=None):
        if weights:
            self.number = len(weights)
            for w in weights:
                self.neuronas.append(Sigmoid(w[:-1], w[-1], learning_rate=self.learning_rate))
            return self
        else:
            if n_inputs is not None:
                for _ in range(self.number):
                    w = []
                    for i in range(n_inputs):
                        w.append(random.random())
                    bias = random.random()
                    self.neuronas.append(Sigmoid(w, bias, learning_rate=self.learning_rate))


    def get_num(self):
        return self.number

    def feed(self, inputs):
        output = list()
        for neuron in self.neuronas:
            output.append(neuron.eval(inputs))
        return output

    def update_last_deltas(self, expected_output):
        for i in range(len(expected_output)):
            error = expected_output[i] - self.neuronas[i].output
            self.neuronas[i].update_delta(error=error)

    def collect_weights(self, collect):
        weights = list()
        for i in range(collect):
            i_weights = list()
            for neuron in self.neuronas:
                i_weights.append(neuron.weight_list[i])
            weights.append(i_weights)
        return weights

    def collect_deltas(self, collect):
        deltas = list()
        for i in range(collect):
            i_deltas = list()
            for neuron in self.neuronas:
                i_deltas.append(neuron.delta)
            deltas.append(i_deltas)
        return deltas

    def collect_outputs(self):
        outputs = list()
        for neuron in self.neuronas:
            outputs.append(neuron.output)
        return outputs

    def update_hidden_deltas(self, weights, deltas):
        for i in range(len(self.neuronas)):
            error = sum(np.array(weights[i]) * np.array(deltas[i]))
            self.neuronas[i].update_delta(error=error)

    def update_neuron_weights(self, inputs):
        for neuron in self.neuronas:
            neuron.update_weights(inputs)

    def update_neuron_bias(self):
        for neuron in self.neuronas:
            neuron.update_bias()
