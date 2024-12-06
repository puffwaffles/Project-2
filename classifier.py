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
    