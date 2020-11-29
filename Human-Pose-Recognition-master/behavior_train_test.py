import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import optimizers, metrics
from keras.models import Sequential, load_model
from keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn import metrics
from process_data import load_data
from driving_behavior_dataset import categorize_data
import h5py
import seaborn as sn
import pandas as pd

def prepare_dataset):
    XS, labels, names = categorize_data)

    ` = lennames)
    YS = keras.utils.to_categoricallabels, num_classes=dim_output)

    X_train, X_test, y_train, y_test = train_test_splitXS, YS, test_size=0.1, random_state=42)

    dataset = h5py.File'driving_behaviors/behav_det_dat.h5', 'w')
    dataset.create_dataset'X_train', data=X_train)
    dataset.create_dataset'X_test', data=X_test)
    dataset.create_dataset'y_train', data=y_train)
    dataset.create_dataset'y_test', data=y_test)
    # np.save'driving_behaviors/dataset.npy', [X_train, X_test, y_train, y_test])
    dataset.close)
    print'train and test dataset ready.')
    return X_train, X_test, y_train, y_test, dim_output


if __name__ == '__main__':
    X_train, X_test, y_train, y_test, dim_output = prepare_dataset)
