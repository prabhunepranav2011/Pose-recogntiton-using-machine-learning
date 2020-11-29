# Human Pose Recognition
1. need to put all docs along with README.txt file in the root directory of your project.
2. Download the dataset from the google drive : https://drive.google.com/drive/folders/1lwT14XXp5c6aJSSshK2mv-Rdyz7WxKH1?usp=sharing
3. run "behavior_train_test.py" to generate the train and test dataset of categorical behavior recognition.
  - RF data is of size (96, 32) in each sample;
  - 10 RF samples together compose a sequential sample, which is of size (10, 96, 32, 1) to represent behavior;
  - 6 categorical behaviors are included in the dataset.
4. run "posetrack_train_test.py" to generate the train and test dataset of pose tracking regression.
  - RF data is of size (96, 32) in each sample;
  - 10 RF samples together compose a sequential sample, which is of size (10, 96, 32, 1) to represent behavior;
  - Joint positions of 12 joints of body part as one sample in the size of (36,) as the ground truth for regression of pose.

