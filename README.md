# Real-Time-Person-Detection

# Getting Started

In this project, we are going to have a simulation about face recognition. The whole structure is divided into 3 parts:

* The general process of working with Yolo version 8
* Working online
* Results
  
# General process

## Installation

YOLOv8 released a package named “ultralytics”, that you can install with the mentioned command below.

pip install ultralytics

## Preparation

You can use this dataset (which was previously in pascal format and i cg]hanged it into yolov8 format) 
https://drive.google.com/drive/folders/1QCzaMMrpBbnpAZCbVex9mfA6NlWLjhx-?usp=drive_link

You can start training YOLOv8 on custom data by using mentioned command below in the terminal/(command prompt).

yolo task=detect mode=train model=yolov8n.pt data=dataset.yaml epochs=25 imgsz=640
task = detect (It can be segment or classify)

mode = train (It can be predict or val)

model = yolov8n.pt (It can yolov8s/yolov8l/yolov8x)

epochs = 25 (It can be any number)

imgsz = 640 (It can be 320, 416, etc, but make sure it needs to be a multiple of 32)

Custom-trained weights will be saved in the folder path mentioned below. runs/train/exp/weights/best.pt

## Start Test

Once your model is trained, you can use it to make predictions on new data. Use the mentioned command below for detection with custom weights.

yolo task=detect mode=predict model="runs/train/exp/weights/best.pt" source="test.png"


# Folder structure:

After running the following code, the folder structure should be as follows: (It is clear that 3 folders train, valid and test are important.)

.
└── dataset
    ├── train
    │   ├── images    
    │   └── labels    
    ├── val    
    │   ├── images    
    │   └── labels    
  
Now create a folder called ‍‍yolov8 and make the previous folders in the following format:
.
├── images
│   ├── train
│   └── valid
├── labels
│   ├── train
│   └── valid

In the yolov8 folder, create a file named dataset.yaml and set the following values in it: (Make sure to set the path according to your folder)

path:  /<PATH-TO>/yolov8/
train: images/train
val: images/valid

#Classes
names:
 0: Person
 
Now all the items are ready and you can train and test it based on the General process section.

Hint: In the ckpts folder, I put two sample yolov8 weights based on yolov8s.pth and 25 trained epochs numbers that you can use as an evaluation.

# Result

![val_batch0_labels](https://github.com/user-attachments/assets/9ecf9eb1-e685-4d92-a591-84349c1b922a)






![val_batch1_pred](https://github.com/user-attachments/assets/3ece0840-3e1e-4b6c-8f37-13ed70d57832)


