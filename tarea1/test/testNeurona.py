from Neurona import Sigmoid, Perceptron
import unittest
import random

class TestNeurona(unittest.TestCase):

    def testPerceptron1(self):
        n = Perceptron([random.uniform(-2., 2.), random.uniform(-2., 2.)], random.uniform(-2., 2.))
        for i in range(50):
            n.training([0., 0.], 0.)
            n.training([0., 1.], 1.)
            n.training([1., 0.], 1.)
            n.training([1., 1.], 1.)
        r1 = n.eval([0., 0.])
        self.assertEqual(r1, 0.)
        r2 = n.eval([0., 1.])
        self.assertEqual(r2, 1.)
        r3 = n.eval([1., 0.])
        self.assertEqual(r3, 1.)
        r4 = n.eval([1., 1.])
        self.assertEqual(r4, 1.)

    def testPerceptron2(self):
        n = Perceptron([random.uniform(-2., 2.), random.uniform(-2., 2.)], random.uniform(-2., 2.))
        for i in range(50):
            n.training([0., 0.], 0.)
            n.training([0., 1.], 0.)
            n.training([1., 0.], 0.)
            n.training([1., 1.], 1.)
        r1 = n.eval([0., 0.])
        self.assertEqual(r1, 0.)
        r2 = n.eval([0., 1.])
        self.assertEqual(r2, 0.)
        r3 = n.eval([1., 0.])
        self.assertEqual(r3, 0.)
        r4 = n.eval([1., 1.])
        self.assertEqual(r4, 1.)

    def testSigmoid1(self):
        n = Sigmoid([random.uniform(-2., 2.), random.uniform(-2., 2.)], random.uniform(-2., 2.))
        for i in range(50):
            n.training([0., 0.], 0.)
            n.training([0., 1.], 0.)
            n.training([1., 0.], 0.)
            n.training([1., 1.], 1.)
        r1 = n.eval([0., 0.])
        self.assertLess(r1, 0.5)
        r2 = n.eval([0., 1.])
        self.assertLess(r2, 0.5)
        r3 = n.eval([1., 0.])
        self.assertLess(r3, 0.5)
        r4 = n.eval([1., 1.])
        self.assertLess(0.5, r4)


