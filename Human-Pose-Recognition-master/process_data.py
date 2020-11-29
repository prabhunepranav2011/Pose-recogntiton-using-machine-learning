import pickle as pkl
import numpy as np
import os
import glob
from sklearn.preprocessing import OneHotEncoder


def load_data():
    step = 2
    length = 10

    Xs = []
    ys = []
    for file_name in glob.iglob(os.getcwd() + '/data/*.pkl'):
        label = int(file_name.split('/')[-1].split('_')[1][0])
        with open(file_name, 'rb') as f:
            X, y = pkl.load(f)
        start = 0
        while start+length < len(X):
            Xs.append(X[start:start+length])
            ys.append(label)
            start += step

    Xs = np.expand_dims(Xs, axis=-1)
    # one hot encode
    onehot_encoded = list()
    unique = np.unique(ys)
    for value in ys:
        letter = [0 for _ in unique]
        letter[value] = 1
        onehot_encoded.append(letter)
    ys = np.asarray(onehot_encoded)

    print(Xs.shape)
    print(ys.shape)

    return Xs, ys


# X, y = load_data()