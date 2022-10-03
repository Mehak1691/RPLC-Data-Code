# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:59:48 2021

@author: 60199
"""

import pandas as pd
import numpy as np
# Importing the dependancies
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def plot_confusion_matrix(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred)
    print(cm)
    cls_cnt = cm.sum(axis=1)
    cls_hit = np.diag(cm)

    cls_acc = cls_hit / cls_cnt.astype(float)
    mean_cls_acc = cls_acc.mean()
    print("Class Accuracy",cls_acc)
    print("Mean Accuracy", mean_cls_acc)
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(
        xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        xticklabels=['Bright', 'Semi-dark', 'Dark'],
        yticklabels=['Bright', 'Semi-dark', 'Dark'],
        title='Confusion Matrix',
        ylabel='True label',
        xlabel='Predicted label'
    )
    plt.setp(
        ax.get_xticklabels(),
        rotation=45,
        ha="right",
        rotation_mode="anchor"
    )
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


df = pd.read_csv('C:/Users/60199/Desktop/Annotated Data/Luminosity_Iteration900_HUNDERED.csv')
y_true=df['Label(Human)']
y_pred=df['Label(Machine)']
class_names = ['B', 'S', 'D']
np.set_printoptions(precision=2)
plot_confusion_matrix(y_true, y_pred, classes=class_names)
plt.show()




