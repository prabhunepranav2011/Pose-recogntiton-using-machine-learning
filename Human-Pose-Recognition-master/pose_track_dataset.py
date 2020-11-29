import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
from keras import optimizers
from keras.models import Sequential, load_model
from keras.layers import TimeDistributed, Conv2D, MaxPooling2D, Flatten, LSTM, Dense
from sklearn.model_selection import train_test_split
from process_data import load_data
import os


def get_dirs():
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'driving_behaviors', 'data1')
    dirs = os.listdir(data_dir)
    return data_dir, dirs


def joint_track_data():
    rfmap_list = []
    depjoint_list = []

    #cwd = os.getcwd()
    dat_root, dirs = get_dirs()

    for dir in dirs:
        # if str(dir) != str("dancing"):
        #     continue
        # print('hello, dancing here')
        dir_dat = os.path.join(dat_root, dir)
        files = os.listdir(dir_dat)
        # f_dat = ''
        X_rf = []
        rfs = []
        joints = []
        for fil in files:
            # print(dir, fil.split('.')[0].split('_')[-1])
            # if fil.split('.')[0].split('_')[-1] == '4':
            #     f_dat = fil
        # file = os.path.join(dat_root, dir, f_dat)
        # # print(file)
        # joints, rf = np.load(file, allow_pickle=True)

            file = os.path.join(dat_root, dir, fil)
            joints_i, rf_i = np.load(file, allow_pickle=True)

            for rf_img in rf_i:
                rfs.append(rf_img)

            for joint_pose in joints_i:
                joints.append(joint_pose)


        # reshape into 1 channel image
        for rf_map in rfs:
            X_rf.append(rf_map.reshape((96, 32, 1)))

        # slicing into sequences
        for i in range(0, len(X_rf) - 10):
            rfmap_list.append([X_rf[i:i + 10]])
            depjoint_list.append(joints[i + 10].reshape(-1))     
    # make type array
    depjoint_list = np.array(depjoint_list)
    rfmap_list = np.array(rfmap_list)
    rfmap_list = rfmap_list.reshape(rfmap_list.shape[0], 10, 96, 32, 1)
    print(np.shape(depjoint_list), np.shape(rfmap_list))
    return rfmap_list, depjoint_list


if __name__ == '__main__':
    rf_maps, dep_joints = joint_track_data()
