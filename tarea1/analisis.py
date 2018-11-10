import pandas as pd
import numpy as np
from NetworkNeurona import NetworkNeurona
import random
import matplotlib.pyplot as plt
import time

def letter_to_num(let):
    a = 0.038
    if let == 'A': return 1*a
    elif let == 'B': return 2*a
    elif let == 'C': return 3*a
    elif let == 'D': return 4*a
    elif let == 'E': return 5*a
    elif let == 'F': return 6*a
    elif let == 'G': return 7*a
    elif let == 'H': return 8*a
    elif let == 'I': return 9*a
    elif let == 'J': return 10*a
    elif let == 'K': return 11*a
    elif let == 'L': return 12*a
    elif let == 'M': return 13*a
    elif let == 'N': return 14*a
    elif let == 'O': return 15*a
    elif let == 'P': return 16*a
    elif let == 'Q': return 17*a
    elif let == 'R': return 18*a
    elif let == 'S': return 19*a
    elif let == 'T': return 20*a
    elif let == 'U': return 21*a
    elif let == 'V': return 22*a
    elif let == 'W': return 23*a
    elif let == 'X': return 24*a
    elif let == 'Y': return 25*a
    elif let == 'Z': return 26*a

def format_data():
    train_l = list()
    train_e = list()
    test_l = list()
    test_e = list()

    ar = pd.read_csv('letter_dataset.csv')
    arreglo_datos = np.array(ar)
    random.shuffle(arreglo_datos)

    count = 0
    for row in range(len(arreglo_datos)):
        if count < 200:
            aux = list()
            aux.append(letter_to_num(arreglo_datos[row][0]))
            train_e.append(aux)
            train_l.append(arreglo_datos[row][1:])
            count+=1
        elif count >= 200 and count < 300:
            aux = list()
            aux.append(letter_to_num(arreglo_datos[row][0]))
            test_e.append(aux)
            test_l.append(arreglo_datos[row][1:])
            count += 1
    return train_l, train_e, test_l, test_e


def create_net(inputs, outs, inner_lay, layers):
    assert layers > 0
    network = list()
    layer1 = list()
    for input_n in range(inner_lay):
        input_neuron = list()
        for n_input in range(inputs + 1):
            input_neuron.append(random.uniform(0, 0.2))
        layer1.append(input_neuron)
    network.append(layer1)
    for layer in range(layers - 2):
        a_layer = list()
        for neuron in range(inner_lay):
            a_neuron = list()
            for _ in range(inner_lay + 1):
                a_neuron.append(random.uniform(0, 0.2))
            a_layer.append(a_neuron)
        network.append(a_layer)
    layern = list()
    for out_n in range(outs):
        output_neuron = list()
        for n_out in range(inner_lay + 1):
            output_neuron.append(random.uniform(0, 0.2))
        layern.append(output_neuron)
    network.append(layern)

    return network


def graficar(train_set, test_set, train_expected, test_expected, iterations=1000, shuffle=True):
    dataset = list()
    for data in zip(train_set, train_expected):
        dataset.append(list(data))

    if shuffle:
        random.shuffle(dataset)

    total_error = list()

    network = create_net(inputs=len(train_set[0]), outs=1, inner_lay=4, layers=3)
    for iteration in range(1, iterations):
        net = NetworkNeurona(manual=True)
        net.initialize(network=network)
        error = net.dataset_train(dataset=dataset, epoch=iteration)
        if error:
            total_error.append(error[-1])
    x_axis = list()
    for i in range(1, iterations):
        x_axis.append(i)
    return x_axis, total_error

er = list()
lr = list()
for i in ([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]):
    lr.append(i)
    train_l, train_e, test_l, test_e = format_data()
    x_axis, total_error = graficar(train_l, test_l, train_e, test_e, 20, True)
    mse = 0
    for a in total_error:
        mse += a**2
    mse.mean(axis=None)
    er.append(mse)
    fig, ax = plt.subplots()
    ax.plot(lr, er, color='r')
    ax.set_xlabel("Learning Rate")
    ax.set_ylabel('Error mean')
plt.title("Letter dataset [Learning Rate v/s Error mean]")
fig.savefig("test8.png")
plt.show()
