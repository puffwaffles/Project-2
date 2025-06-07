import pandas as pd
from queue import PriorityQueue
import numpy as np
from classifier import*

class Validator:
    def __init__(self, features, classifier, dataset):
        self.features = features
        self.classifier = classifier
        self.dataset = dataset

    """
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
    """

    #Evaluation function 
    def evaluate(self): 
        acc = 0.0
        correct = 0.0
        vallist = self.classifier.test()
        #Iterate through each instance row
        for i in range(len(self.dataset)):
            #Correct instance class
            correctacc = self.dataset[i][0]

            #Sort the list for i based on distance
            sort = sorted(vallist[i], key = lambda x: x[1])
            #Predicted instance class
            predictacc = sort[0][0]

            #Increment correct if correctacc and predictacc match
            if (correctacc == predictacc):
                correct = correct + 1

        #Evaluate proportion of correct guesses
        acc = correct / len(self.dataset)
        #Convert acc to negative percentage for priority queue
        acc = round(acc * 100, 1) * -1
        return acc    

    #Default rate function
    def default(self):
        classvalues = {}
        defaultacc = 0.0
        amount = 0
        total = len(self.dataset)
        #Iterate through class values to find them 
        for i in range(len(self.dataset)):
            #If we have not found this class value yet, add the vlaue to the map 
            if (self.dataset[i][0] not in classvalues):
                classvalues.update({self.dataset[i][0]: 1})
            #Otherwise, increment the instances of the value
            else:
                classvalues.update({self.dataset[i][0]: classvalues.get(self.dataset[i][0]) + 1})
        #Find the total amount of instances of the most common class
        for j in classvalues:
            if (classvalues[j] > amount):
                amount = classvalues[j]
        #Default rate is the #most common class / total amount of instances
        defaultacc = amount / total
        defaultacc = round(defaultacc * 100, 1) * -1
        return defaultacc