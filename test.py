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
import time

numfeatures = promptnumfeatures()
newdata = []
featurelist = promptfeatures(numfeatures)
data = promptdataset()
acc = 0.0
badval = False
match data:
    case 1:
        file = 'data/small-test-dataset.txt'
        start = time.time()
        newdata = normalize(file) 
        end = time.time()
        print(f"Time taken for normalization: {end - start}")
        for i in range(len(featurelist)):
            if (featurelist[i] < 1 or featurelist[i] >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the small test dataset")
        else:
            classify = Classifier(featurelist, newdata)
            validate = Validator(featurelist, classify, classify.gettrainingdata())
            default = validate.default()
            print(f"Default rate: {default * -1}")
            start = time.time()
            acc = validate.evaluate() * -1
            end = time.time()
            print(f"Time taken for validation: {end - start}")
            print(f"After normalizing and running nn, we get an accuracy of {acc}% for small test dataset")
            newrawdata = raw(file)
            newclassify = Classifier(featurelist, newrawdata)
            newvalidate = Validator(featurelist, newclassify, newclassify.gettrainingdata())
            default = newvalidate.default()
            print(f"Default rate: {default * -1}")
            acc = validate.evaluate() * -1
            print(f"Without normalizing and running nn, we get an accuracy of {acc}% for small test dataset")
    case 2:
        file = 'data/large-test-dataset.txt'
        start = time.time()
        newdata = normalize(file) 
        end = time.time()
        print(f"Time taken for normalization: {end - start}")
        for i in range(len(featurelist)):
            if (featurelist[i] < 1 or featurelist[i] >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the large test dataset")
        else:
            classify = Classifier(featurelist, newdata)
            validate = Validator(featurelist, classify, classify.gettrainingdata())
            default = validate.default()
            print(f"Default rate: {default * -1}")
            start = time.time()
            acc = validate.evaluate() * -1
            end = time.time()
            print(f"Time taken for validation: {end - start}")
            print(f"After normalizing and running nn, we get an accuracy of {acc}% for large test dataset")
            newrawdata = raw(file)
            newclassify = Classifier(featurelist, newrawdata)
            newvalidate = Validator(featurelist, newclassify, newclassify.gettrainingdata())
            default = newvalidate.default()
            print(f"Default rate: {default * -1}")
            acc = validate.evaluate() * -1
            print(f"Without normalizing and running nn, we get an accuracy of {acc}% for large test dataset")
    case 3: 
        file = 'data/titanic-clean.txt'
        start = time.time()
        newdata = normalize(file) 
        end = time.time()
        print(f"Time taken for normalization: {end - start}")
        for i in range(len(featurelist)):
            if (featurelist[i] < 1 or featurelist[i] >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the titanic test dataset")
        else:
            classify = Classifier(featurelist, newdata)
            validate = Validator(featurelist, classify, classify.gettrainingdata())
            default = validate.default()
            print(f"Default rate: {default * -1}")
            start = time.time()
            acc = validate.evaluate() * -1
            end = time.time()
            print(f"Time taken for validation: {end - start}")
            print(f"After normalizing and running nn, we get an accuracy of {acc}% for titanic test dataset")
            newrawdata = raw(file)
            newclassify = Classifier(featurelist, newrawdata)
            newvalidate = Validator(featurelist, newclassify, newclassify.gettrainingdata())
            default = newvalidate.default()
            print(f"Default rate: {default * -1}")
            acc = validate.evaluate() * -1
            print(f"Without normalizing and running nn, we get an accuracy of {acc}% for titanic test dataset")
    case default:
        print("Invalid input!")

