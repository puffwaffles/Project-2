from queue import PriorityQueue
import node 
import numpy as np
import pandas as pd
import sys
import time

#Checks if a list already exists in the dictionary
def alreadyexists(currlist, usedlists):
    exists = False
    tuplelist = (*currlist, )
    if (tuplelist in usedlists):
        exists = True
    return exists
    
#Returns list of unselected features
def remaining(currlist, fulllist):
    remain = []
    if (len(currlist) == 0):
        remain = fulllist.copy()
    else:
        remain = list(set(fulllist) - set(currlist))
    return remain

#Just gets raw data
def raw(dataset):
    newdatadf = pd.read_csv(dataset, sep='\s+', header=None)
    newdatadf.astype(float)
    print()
    print(f"This dataset has {newdatadf.shape[1] - 1} features (not including the class attribute), with {newdatadf.shape[0]} instances.")
    print()
    sys.stdout.write("Please wait while I gather the data... ")
    newdata = []
    #Rows
    for i in range(newdatadf.shape[0]):
        row = []
        #Columns
        for j in range(newdatadf.shape[1]):
            row.append(float(newdatadf.iloc[i, j]))
        newdata.append(row)
    sys.stdout.write("Done!")
    print()
    return newdata

#Takes in dataset to normalize it
def normalize(dataset):
    newdatadf = pd.read_csv(dataset, sep='\s+', header=None)
    newdatadf.astype(float)
    print()
    print(f"This dataset has {newdatadf.shape[1] - 1} features (not including the class attribute), with {newdatadf.shape[0]} instances.")
    print()
    sys.stdout.write("Please wait while I normalize the data... ")
    newdata = []
    minimum = []
    maximum = []
    #Gather min and max values for each column
    for k in range(newdatadf.shape[1]):
        coldf = newdatadf.iloc[:, k]
        minimum.append(coldf.min())
        maximum.append(coldf.max())
    #Rows
    for i in range(newdatadf.shape[0]):
        row = []
        #Columns
        for j in range(newdatadf.shape[1]):
            if (j == 0): 
                row.append(float(newdatadf.iloc[i, 0]))
            else:
                oldnum = float(newdatadf.iloc[i, j])
                num = float((oldnum - minimum[j]) / (maximum[j] - minimum[j]))
                row.append(num)
        newdata.append(row)
    sys.stdout.write("Done!")
    print()
    return newdata

#Change list of np.int64() to list of int
def convertint(oldlist):
    newlist = oldlist
    for i in range(len(newlist)):
        if (isinstance(newlist[i], int) == False):
            newlist[i] = newlist[i].item()
    return newlist