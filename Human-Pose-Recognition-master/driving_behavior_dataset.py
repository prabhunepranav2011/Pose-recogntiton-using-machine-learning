import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
from keras import optimizers
from keras.models import Sequential, load_model
from keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense
from sklearn.model_selection import train_test_split
from process_data import load_data
import os
import pdb


def get_dirs():
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'driving_behaviors', 'data1')
    dirs = os.listdir(data_dir)
    return data_dir, dirs


def categorize_data():
    rfmap_list = []
    category_list = []

    #cwd = os.getcwd()
    dat_root, dirs = get_dirs()

    for ix, dir in enumerate(dirs):
        target = ix
        print('category: ', dir)

        dir_dat = os.path.join(dat_root, dir)
        files = os.listdir(dir_dat)
        f_dat = ''
        X_rf = []
        # joints = []
        rfs = []
        for fil in files:

            print (fil)
            print(dir, fil.split('.')[0].split('_')[-1])
            # if fil.split('.')[0].split('_')[-1] == '0':
            f_dat = fil
        file = os.path.join(dat_root, dir, f_dat)
        #     print(fil)
        print("file name for load - ",file)
        joints, rfs = np.load(file, allow_pickle=True)
            # file = os.path.join(dat_root, dir, fil)
            # joints_i, rf_i = np.load(file, allow_pickle=True)
            # for rf_img in rf_i:
            #     rfs.append(rf_img)
        # X_rf = []
        for rf_map in rfs:
            X_rf.append(rf_map.reshape((96, 32, 1)))
        for i in range(0, len(X_rf) - 10):

            rfmap_list.append([X_rf[i:i + 10]])
            category_list.append(target)

    category_list = np.array(category_list)
    rfmap_list = np.array(rfmap_list)
    rfmap_list = rfmap_list.reshape(rfmap_list.shape[0], 10, 96, 32, 1)
    print("categorical behavior data ready.", np.shape(category_list), np.shape(rfmap_list))
    return rfmap_list, category_list, dirs


if __name__ == '__main__':
    rfmaps, categories, behavior_names = categorize_data()
