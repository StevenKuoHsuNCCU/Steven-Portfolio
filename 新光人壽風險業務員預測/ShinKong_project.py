# Imported Libraries

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import time

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import collections

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from imblearn.pipeline import make_pipeline as imbalanced_make_pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report
from collections import Counter
from sklearn.model_selection import KFold, StratifiedKFold
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import GridSearchCV


import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense, Dropout, Conv2D, MaxPooling1D, Flatten, Conv1D
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy

from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pycaret.classification import *
from matplotlib import cm
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, pair_confusion_matrix


df = pd.read_csv("/Users/stevenkuo/College Course/大三/人工智慧與機器學習實作/final_with_agent_no.csv")

def rename_first_func(df):
    original_columns = list(df.columns)
    original_columns[0] = 'number'
    df.columns = original_columns
    return df

df = rename_first_func(df)


dd = df.copy()


df = df.drop("serial_no", axis=1)
df = df.drop("number", axis=1)





def SMOTE_LOG_KERAS_METHOD(df, batch, epoch):
    
    ########## View the percentage of abnormal target in the data ##########
    
    #print('Normal', round(df['abnormal_target'].value_counts()[0]/len(df) * 100,2), '% of the dataset')
    #print('Abnormal', round(df['abnormal_target'].value_counts()[1]/len(df) * 100,2), '% of the dataset')
    
    
    X = df.drop('abnormal_target', axis=1)
    y = df['abnormal_target']

    sss = StratifiedKFold(n_splits=5, random_state=None, shuffle=True)

    for train_index, test_index in sss.split(X, y):
        original_Xtrain, original_Xtest = X.iloc[train_index], X.iloc[test_index]
        original_ytrain, original_ytest = y.iloc[train_index], y.iloc[test_index]
        
        
    original_Xtrain = original_Xtrain.values
    original_Xtest = original_Xtest.values
    original_ytrain = original_ytrain.values
    original_ytest = original_ytest.values

    

    # SMOTE Technique (OverSampling) After splitting and Cross Validating
    sm = SMOTE(sampling_strategy='minority', random_state= False)


    Xsm_train, ysm_train = sm.fit_resample(original_Xtrain, original_ytrain)
    
    n_inputs = Xsm_train.shape[1]

    oversample_model = Sequential([
        
        Conv1D(filters=15, kernel_size=1, activation='relu', input_shape=(n_inputs, 1)),
        # Add MaxPooling1D layer
        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        # Flatten the output before passing to the dense layers
        
        Flatten(),
        
        
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dropout(0.2),
        Dense(2, activation='softmax')
        ])

    oversample_model.compile(Adam(lr=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    oversample_model.fit(Xsm_train, ysm_train, validation_split=0.3, batch_size=batch, epochs=epoch, shuffle=True, verbose=0)


    # Assuming oversample_model is your TensorFlow/Keras model
    oversample_fraud_predictions = oversample_model.predict(original_Xtest, batch_size=batch, verbose=0)
    oversample_fraud_predictions = oversample_fraud_predictions.argmax(axis=-1)

    accuracy = accuracy_score(original_ytest, oversample_fraud_predictions)
    precision = precision_score(original_ytest, oversample_fraud_predictions)
    recall = recall_score(original_ytest, oversample_fraud_predictions)
    f1 = f1_score(original_ytest, oversample_fraud_predictions)
    
    
    
    return accuracy, precision, recall, f1
    

def model_exp(df, batch, epoch):
    
    accuracy_list = list()
    precision_list = list()
    recall_list = list()
    f1_list = list()
    
    for i in range(0,10):
        
        accuracy, precision, recall, f1  = SMOTE_LOG_KERAS_METHOD(df, batch, epoch)
        
        accuracy_list.append(accuracy)
        precision_list.append(precision)
        recall_list.append(recall)
        f1_list.append(f1)
        
    
    return np.mean(accuracy_list), np.mean(precision_list), np.mean(recall_list), np.mean(f1_list), np.std(accuracy_list), np.std(precision_list), np.std(recall_list), np.std(f1_list)
        



def start(df):
    data4_exp_record = pd.DataFrame()
    l_batch = list()
    l_epoch = list()
    l1 = list()
    l2 = list()
    l3 = list()
    l4 = list()
    l5 = list()
    l6 = list()
    l7 = list()
    l8 = list()
    
    for batch in range(1800, 2400, 200):
        for epoch in range(10, 30, 5):
            
            d1, d2, d3, d4, d5, d6, d7, d8 = model_exp(df, batch, epoch)
            
            l_batch.append(batch)
            l_epoch.append(epoch)
            l1.append(d1)
            l2.append(d2)
            l3.append(d3)
            l4.append(d4)
            l5.append(d5)
            l6.append(d6)
            l7.append(d7)
            l8.append(d8)
            
            
    data4_exp_record["accuracy_mean"] = l1
    data4_exp_record["precision_mean"] = l2
    data4_exp_record["recall_mean"] = l3
    data4_exp_record["f1_mean"] = l4
    data4_exp_record["accuracy_std"] = l5
    data4_exp_record["precision_std"] = l6
    data4_exp_record["recall_std"] = l7
    data4_exp_record["f1_std"] = l8
    data4_exp_record["batch"] = l_batch
    data4_exp_record["epoch"] = l_epoch
    
    
    data4_exp_record.to_csv("zzz_exp_record.csv", index=False)





def catch_fraud(df, batch, epoch):
    
    ########## View the percentage of abnormal target in the data ##########
    
    #print('Normal', round(df['abnormal_target'].value_counts()[0]/len(df) * 100,2), '% of the dataset')
    #print('Abnormal', round(df['abnormal_target'].value_counts()[1]/len(df) * 100,2), '% of the dataset')
    
    
    X = df.drop('abnormal_target', axis=1)
    y = df['abnormal_target']

    sss = StratifiedKFold(n_splits=5, random_state=None, shuffle=True)

    for train_index, test_index in sss.split(X, y):
        original_Xtrain, original_Xtest = X.iloc[train_index], X.iloc[test_index]
        original_ytrain, original_ytest = y.iloc[train_index], y.iloc[test_index]
        
        
    original_Xtrain = original_Xtrain.values
    original_Xtest = original_Xtest.values
    original_ytrain = original_ytrain.values
    original_ytest = original_ytest.values

    

    # SMOTE Technique (OverSampling) After splitting and Cross Validating
    sm = SMOTE(sampling_strategy='minority', random_state= False)


    Xsm_train, ysm_train = sm.fit_resample(original_Xtrain, original_ytrain)
    
    n_inputs = Xsm_train.shape[1]

    oversample_model = Sequential([
        
        Conv1D(filters=15, kernel_size=1, activation='relu', input_shape=(n_inputs, 1)),
        # Add MaxPooling1D layer
        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        # Flatten the output before passing to the dense layers
        
        Flatten(),
        
        
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(32, activation='relu'),
        Dropout(0.2),
        Dense(2, activation='softmax')
        ])

    oversample_model.compile(Adam(lr=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    oversample_model.fit(Xsm_train, ysm_train, validation_split=0.3, batch_size=batch, epochs=epoch, shuffle=True, verbose=0)


    # Assuming oversample_model is your TensorFlow/Keras model
    oversample_fraud_predictions = oversample_model.predict(original_Xtest, batch_size=batch, verbose=0)
    oversample_fraud_predictions = oversample_fraud_predictions.argmax(axis=-1)

    accuracy = accuracy_score(original_ytest, oversample_fraud_predictions)
    precision = precision_score(original_ytest, oversample_fraud_predictions)
    recall = recall_score(original_ytest, oversample_fraud_predictions)
    f1 = f1_score(original_ytest, oversample_fraud_predictions)
    
    
    
    ll = pd.DataFrame()
    ll["index"] = test_index
    ll["real"] = original_ytest
    ll["predict"] = oversample_fraud_predictions
    
    pre_g = ll[ll["predict"] == 1]["index"].values
    per_b = ll[ll["predict"] == 0]["index"].values
    
    
    a = test_index.tolist()
    b = original_ytest.tolist()
    c = oversample_fraud_predictions.tolist()
    
    return a, b, c


cc = pd.read_csv("/Users/stevenkuo/College Course/大三/人工智慧與機器學習實作/result_summary.csv")

ee = cc[cc["predict_1_percentage"] == 100 ]

ff = ee[ee["real"] != 1]

#hh = ff[ff["test_count"]]

print(ff.index)

for i in dd.iloc[ff.index, 1]:
    print(i)

#print(dd[dd["serial_no"] == "agnt_0070"])


'''


lot = pd.DataFrame()

test = list()
org = list()
pred = list()

for i in range(0,1000):
    test_people , org_people, pred_people = catch_fraud(df, 2200, 20)
    test.extend(test_people)
    org.extend(org_people)
    pred.extend(pred_people)
    
    
lot["test_people"] = test
lot["real"] = org
lot["predict"] = pred

lot.to_csv("zzz_final_fraud_1000.csv", index=False)


'''





















