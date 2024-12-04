#For function testing purposes
from forward import*
from backward import*
from listfuncs import*
from classifier import*
from menu import*
from node import*
import pandas as pd
import sys

newdata = []
newdata = normalize('data/small-test-dataset.txt') 
featureslist = [1, 4, 6, 9]
for i in range(3):
    for j in range(len(newdata[i])):
        sys.stdout.write(str(newdata[i][j]))
        sys.stdout.write(' ')
    print()
classify = Classifier(featureslist, newdata)
traineddata = classify.gettrainingdata()
for i in range(3):
    for j in range(len(traineddata[i])):
        sys.stdout.write(str(traineddata[i][j]))
        sys.stdout.write(' ')
    print()
instance = 15
print(f"Actual class: {traineddata[instance][0]}")
iclass = classify.test(instance)
print(f"Classifier guesses: {iclass}")
