from unittest import TestCase

from NetworkNeurona import NetworkNeurona

class TestNetwork(TestCase):
    network = NetworkNeurona()

    def test_add_layer(self):
        self.assertEqual(len(self.network.layers), 0)
        self.network.add_layer(10)
        self.assertEqual(len(self.network.layers), 1)

    def test_initialized(self):
        self.network = NetworkNeurona()
        self.network.add_layer(4)
        self.network.add_layer(4)
        self.network.initialize(10)
        self.assertTrue(self.network.initialized)
        self.assertIs(self.network.layer1, self.network.layers[0])
        self.assertIs(self.network.layern, self.network.layers[-1])

    def setUpNet1(self):
        self.network = NetworkNeurona()
        self.network.add_layer(3)
        self.network.add_layer(4)
        self.network.initialize(2)

    def setUpNet2(self):
        self.network = NetworkNeurona()
        self.network.add_layer(3)
        self.network.add_layer(1)
        self.network.initialize(2)

    def test_feed(self):
        self.setUpNet1()
        out = self.network.feed([4, 7])
        self.assertEqual(len(out), 4)

    def test_layers(self):
        self.setUpNet2()
        self.assertEqual(len(self.network.layers[0]), 3)
        self.assertEqual(len(self.network.layers[1]), 1)


    def test_xor(self):
        self.setUpNet2()

        epoch = 1000
        self.network.dataset_train(dataset=[
            [[0., 0.], [0]],
            [[1., 1.], [0]],
            [[1., 0.], [1]],
            [[0., 1.], [1]]
        ], epoch=epoch)

        print("XOR(1,1) = {}".format(self.network.feed([1., 1.])[0]))
        print("XOR(1,0) = {}".format(self.network.feed([1., 0.])[0]))
        print("XOR(0,1) = {}".format(self.network.feed([0., 1.])[0]))
        print("XOR(0,0) = {}".format(self.network.feed([0., 0.])[0]))
