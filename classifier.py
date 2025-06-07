import pandas as pd
from queue import PriorityQueue
import numpy as np
import sys

class Classifier:

    def __init__(self, features, dataset):
        self.features = features
        self.dataset = dataset
        self.training = []
        self.train()

    def train(self):
        k = 0
        #Iterate through rows of dataset
        for i in range(len(self.dataset)):
            #Add new row to training set
            self.training.append([])
            #Iterate through columns of dataset
            for j in range(len(self.dataset[i])):
                #Check if value column is part of the feature list or is class value
                if (j == 0 or j in self.features):
                    #Add the value to the training dataset
                    self.training[i].append(self.dataset[i][j])


    def gettrainingdata(self):
        return self.training

    def getfeatures(self):
        return self.features

    """
    def test(self, instance):
        classify = 0.0
        smallest = sys.float_info.max
        for i in range(len(self.training)):
            if (i != instance):
                trainclass = self.training[i][0]
                list1 = self.training[i][1:]
                list2 = self.training[instance][1:]
                dist = np.linalg.norm(np.array(list1) - np.array(list2))
                if (dist < smallest):
                    classify = trainclass
                    smallest = dist
        return classify
    """
    def test(self):
        #Dictionary that stores dictionary of distance lists for each data point
        vallist = {}
        #Grab elements from 0 to size - 1
        for i in range(len(self.training) - 1):
            #Grab elements from i + 1 to size. We avoid grabbing the same elements as i and parallelize on pairs
            for j in range(i + 1, len(self.training)):
                #Get classes of i and j
                trainclass1 = self.training[i][0]
                trainclass2 = self.training[j][0]

                #Get feature values for i and j
                list1 = self.training[i][1:]
                list2 = self.training[j][1:]
                
                #Compute euclidean distance between i and j
                dist = np.linalg.norm(np.array(list1) - np.array(list2))

                #Append class of j and distance in i's list
                if (i not in vallist.keys()):
                    vallist[i] = [[trainclass2, dist]]
                else:
                    vallist[i].append([trainclass2, dist])

                #Append class of i and distance in j's list
                if (j not in vallist.keys()):
                    vallist[j] = [[trainclass1, dist]]
                else:
                    vallist[j].append([trainclass1, dist])
        return vallist