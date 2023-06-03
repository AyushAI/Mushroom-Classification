# **Mushroom Classification**

This repository contains a machine learning model trained to classify mushrooms as edible or poisonous based on certain features. The model is implemented using a decision tree algorithm.

# Dataset
The dataset used for training and testing the model consists of samples of mushrooms, where each sample is characterized by the following input features:
- Gill Size
- Gill Color
- Stalk Root
- Spore Print Color
- Population

The target variable is the classification of the mushroom as either **"edible"** or **"poisonous"**.

Link: https://www.kaggle.com/datasets/uciml/mushroom-classification

# Model

The decision tree algorithm was chosen for this classification task.

# Documentation

High Level Design: https://drive.google.com/file/d/1iLrf1ZUaNPPa-mjn1JahB5w-HtwV7tr9/view?usp=sharing

Low Level Design:
https://drive.google.com/file/d/12z1qmOYUQLM7Q2ExHxupxPrXXYjsDIg5/view?usp=sharing

Project Report: https://drive.google.com/file/d/1f2KHrvaOmvVcZhhard7T4qq7Ys_Qf560/view?usp=sharing

Depolyment Process: https://drive.google.com/file/d/1W9mAdjQe7RUdEEmGg7t0EqnZkyrP4u7G/view?usp=sharing

Architecture: https://drive.google.com/file/d/1kMYoN3DvkIMtqwvjl0m25meHQSh-Cq-D/view?usp=sharing

Model Traning: https://drive.google.com/file/d/1blWa-SEbEnkigeWIOPwlmmkUGxL6cQGM/view?usp=sharing

# Usage
To use this project, follow these steps:

1. Run <code>pip install virtualenv </code>
2. Create a python Virtual environment:
<code>virtualenv envname</code>
3. To activate the environment:<br>
a: <code>cd envname</code><br>
b: <code>Scripts\activate</code>
4. Move back to Main directory:
<code>cd ..</code>
5. Install required libraries:
<code>pip install -r requirements.txt</code>
6. Run the app:
<code>python app.py</code>

# Confusion Matrix
Below is the confusion matrix for the decision tree model:

<img src='./download.png' height="400">
