# -*- coding: utf-8 -*-
"""datasetLoad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-8BD3FF4pKdVkU76Os4uTg74F9yszWHU
"""

import tensorflow as tf
print(tf.__version__)

import pickle as pkl

import numpy as np

print(np.__version__)

import pandas as pd

import glob

from sklearn.model_selection import train_test_split

from google.colab import drive 
drive.mount('/content/drive')

def get_dirs():
    cwd = os.getcwd()
    data_dir = os.path.join(cwd,'drive','My Drive','driving_behaviors', 'data1')
    dirs = os.listdir(data_dir)
    return data_dir, dirs

def joint_track_data():
    dat_root, dirs = get_dirs()
    totalData = []
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

        print("directory ",dir)
        for fil in files:
            # print(dir, fil.split('.')[0].split('_')[-1])
            # if fil.split('.')[0].split('_')[-1] == '4':
            #     f_dat = fil
        # file = os.path.join(dat_root, dir, f_dat)
        # # print(file)
        # joints, rf = np.load(file, allow_pickle=True)

            file = os.path.join(dat_root, dir, fil)
            joints_i, rf_i = np.load(file, allow_pickle=True)

            joint_loc = []
            joint_test_loc = []
            for joint_pose in joints_i:
                joints.append(joint_pose)
            count = 0;
            jts = []
            X_train, X_test = train_test_split(joints, test_size=0.1, random_state=42)
            for jt in joints:
                jts = jt.reshape(-1)
                joint_loc.append(jts)
            print(np.shape(joint_loc))
            for jtest in X_test:
            	joint_test_loc.append(jtest.reshape(-1))
            cwd = os.getcwd()
            name = "/content/drive/My Drive/train/"+dir+".csv"
            nameTest ="/content/drive/My Drive/test/"+dir+"test.csv"
            print(name,"  ",nameTest)
            
            np.savetxt(nameTest,joint_test_loc,delimiter=",",header="head_1_x,head_1_y,head_1_z,head_2_x,head_2_y,head_2_z,head_3_x,head_3_y,head_3_z,head_4_x,head_4_y,head_4_z,left_1_x,left_1_y,left_1_z,left_2_x,left_2_y,left_2_z,left_3_x,left_3_y,left_3_z,left_4_x,left_4_y,left_4_z,right_1_x,right_1_y,right_1_z,right_2_x,right_2_y,right_2_z,right_3_x,right_3_y,right_3_z,right_4_x,right_4_y,right_4_z",comments = "",fmt = ' %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f')
            np.savetxt(name, joint_loc, delimiter=",",header="head_1_x,head_1_y,head_1_z,head_2_x,head_2_y,head_2_z,head_3_x,head_3_y,head_3_z,head_4_x,head_4_y,head_4_z,left_1_x,left_1_y,left_1_z,left_2_x,left_2_y,left_2_z,left_3_x,left_3_y,left_3_z,left_4_x,left_4_y,left_4_z,right_1_x,right_1_y,right_1_z,right_2_x,right_2_y,right_2_z,right_3_x,right_3_y,right_3_z,right_4_x,right_4_y,right_4_z",comments = "",fmt = ' %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f, %.8f')
            
            data = pd.read_csv(name)
            data.insert(36,'Name',dir)
            data.drop(data.index[0])
            data.to_csv(name,index=False)

            test_data = pd.read_csv(nameTest)
            test_data.insert(36,'Name',dir)
            test_data.to_csv(nameTest,index = False)

import os

def createDatasetFile():
	cwd = os.getcwd()
	# Merging data into single dataset
	data_dir = "/content/drive/My Drive/train/"+"*.csv"
	dirs = glob.glob(data_dir)
	df = pd.concat((pd.read_csv(f, header = 0) for f in dirs))
	df.to_csv("/content/drive/My Drive/dataset/output.csv",index=False)
    
    #Merging test data into single dataset 
	data_test_dir = "/content/drive/My Drive/test/"+"*.csv"
	test_dirs = glob.glob(data_test_dir)
	df = pd.concat((pd.read_csv(f,header = 0) for f in test_dirs))
	df.to_csv("/content/drive/My Drive/dataset/testing.csv",index=False)

if __name__ == '__main__':
   joint_track_data()
   createDatasetFile()

"""/content/drive/My Drive/test/turning_righttest.csv"""