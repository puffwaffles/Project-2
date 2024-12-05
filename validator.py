import pandas as pd
from queue import PriorityQueue
import numpy as np
from classifier import*

class Validator:
    def __init__(self, features, classifier, dataset):
        self.features = features
        self.classifier = classifier
        self.dataset = dataset

    #Evaluation function 
    def evaluate(self): 
        acc = 0.0
        correct = 0.0
        #Iterate through each instance row
        for i in range(len(self.dataset)):
            #Correct instance class
            correctacc = self.dataset[i][0]
            #Predicted instance class
            predictacc = self.classifier.test(i)
            #Increment correct if correctacc and predictacc match
            if (correctacc == predictacc):
                correct = correct + 1
        #Evaluate proportion of correct guesses
        acc = correct / len(self.dataset)
        #Convert acc to negative percentage for priority queue
        acc = round(acc * 100, 1) * -1
        return acc