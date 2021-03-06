#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#features_train = features_train[:len(features_train)/50] 
#labels_train = labels_train[:len(labels_train)/50] 

#########################################################
### your code goes here ###
from sklearn.svm import SVC
import numpy as np
#clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print( "training time: ", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print( "predict time: ", round(time()-t1, 3), "s")
#print( pred[10] )
#print( pred[26] )
#print( pred[50] )
chrisPredictions = np.array(pred[pred == 1])
sharaPredictions = np.array(pred[pred == 0])
print( "ChrisEmails:", chrisPredictions.size)
print( "sharaEmails:", sharaPredictions.size)

accuracy = clf.score(features_test, labels_test)
print(accuracy)


#########################################################


