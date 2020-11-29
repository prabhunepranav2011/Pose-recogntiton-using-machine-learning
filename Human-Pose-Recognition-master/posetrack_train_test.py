import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import optimizers
from keras.models import Sequential, load_model
from keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, \
    LSTM, Dense, ConvLSTM2D, BatchNormalization, Dropout
from sklearn.model_selection import train_test_split
from process_data import load_data
from pose_track_dataset import joint_track_data
import h5py

def prepare_dataset():
    XS, YS = joint_track_data()


    dim_output = YS.shape[-1]
    # YS = keras.utils.to_categorical(labels, num_classes=dim_output)

    X_train, X_test, y_train, y_test = train_test_split(XS, YS, test_size=0.1, random_state=42)

    dataset = h5py.File('driving_behaviors/dataset.h5', 'w')
    dataset.create_dataset('X_train', data=X_train)
    dataset.create_dataset('X_test', data=X_test)
    dataset.create_dataset('y_train', data=y_train)
    dataset.create_dataset('y_test', data=y_test)
    # np.save('driving_behaviors/dataset.npy', [X_train, X_test, y_train, y_test])
    dataset.close()
    print(' posetrack train and test dataset ready...')
    return X_train, X_test, y_train, y_test, dim_output

if __name__ == '__main__':
    X_train, X_test, y_train, y_test, dim_output = prepare_dataset()
    print("train shape X ",np.shape(X_train))
    print("test shape X ",np.shape(X_test))
    print("train shape y ",np.shape(y_train))
    print("test shape y ",np.shape(y_test))