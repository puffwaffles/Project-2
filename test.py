#For function testing purposes
from forward import*
from backward import*
from listfuncs import*
from validator import*
from classifier import*
from menu import*
from node import*
import pandas as pd
import sys

numfeatures = promptnumfeatures()
newdata = []
featurelist = promptfeatures(numfeatures)
data = promptdataset()
acc = 0.0
badval = False
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt') 
        for i in range(len(featurelist)):
            if (featurelist[i] < 1 or featurelist[i] > len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the small test dataset")
        else:
            classify = Classifier(featurelist, newdata)
            validate = Validator(featurelist, classify, classify.gettrainingdata())
            acc = validate.evaluate() * -1
            print(f"After running nn, we get an accuracy of {acc}% for small test dataset")
    case 2:
        newdata = normalize('data/large-test-dataset.txt')
        for i in range(len(featurelist)):
            if (featurelist[i] < 1 or featurelist[i] > len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the large test dataset")
        else:
            classify = Classifier(featurelist, newdata)
            validate = Validator(featurelist, classify, classify.gettrainingdata())
            acc = validate.evaluate() * -1
            print(f"After running nn, we get an accuracy of {acc}% for large test dataset")
    case default:
        print("Invalid input!")

