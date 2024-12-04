from queue import PriorityQueue
import node 
import numpy as np
import pandas as pd

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

#Takes in dataset to normalize it
def normalize(dataset):
    newdatadf = pd.read_csv(dataset, sep='\s+', header=None)
    newdatadf.astype(float)
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
    return newdata