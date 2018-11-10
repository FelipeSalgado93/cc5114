from CapaNeurona import CapaNeurona


class NetworkNeurona:
    def __init__(self, manual=False, learning_rate=0.5):
        self.layers = list()
        self.layer1 = None
        self.layern = None
        self.manual = manual
        self.initialized = False
        self.learning_rate = learning_rate

    def add_layer(self, neuron_number):
        if not self.initialized:
            if not self.manual:
                self.layers.append(CapaNeurona(number=neuron_number, learning_rate=self.learning_rate))

    def initialize(self, n_inputs=None, network=None):
        if not self.manual:
            if len(self.layers) > 0:

                self.layers[0].initialize(n_inputs)
                for i in range(1, len(self.layers)):
                    self.layers[i].initialize(self.layers[i - 1].get_num())
                self.layer1 = self.layers[0]
                self.layern = self.layers[len(self.layers) - 1]
                self.initialized = True
        else:
            if network is not None:
                assert len(network) > 0
                if len(network) > 1:
                    assert (len(network[-1][0]) - 1) == (len(network[-2]))

                for layer in network:
                    self.layers.append(CapaNeurona(learning_rate=self.learning_rate).initialize(weights=layer))
                self.layer1 = self.layers[0]
                self.layern = self.layers[len(self.layers) - 1]

                self.initialized = True

    def feed(self, inputs):
        out = self.layer1.feed(inputs)
        for layer in self.layers:
            if layer is not self.layer1:
                out = layer.feed(out)
        return out

    def train(self, inputs, expected_output):
        output = self.feed(inputs)
        self.layern.update_last_deltas(expected_output=expected_output)
        for i in range(len(self.layers) - 2, -1, -1):
            weights_collection = self.layers[i + 1].collect_weights(collect=self.layers[i].get_num())
            delta_collection = self.layers[i + 1].collect_deltas(collect=self.layers[i].get_num())
            print(delta_collection)
            self.layers[i].update_hidden_deltas(weights=weights_collection, deltas=delta_collection)
        self.layer1.update_neuron_weights(inputs=inputs)
        self.layer1.update_neuron_bias()

        for j in range(1, len(self.layers)):
            output_collection = self.layers[j - 1].collect_outputs()
            self.layers[j].update_neuron_weights(output_collection)
            self.layers[j].update_neuron_bias()

        return sum([(expected_output[i] - output[i]) ** 2 for i in range(len(expected_output))])

    def dataset_train(self, dataset, epoch):
        error = list()
        for _ in range(epoch):
            local_error = 0
            for data in dataset:
                local_error += self.train(data[0], data[1])
            error.append(local_error)
        return error
