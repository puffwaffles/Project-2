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

def converttodf(data):
    columns = []
    for i in range(len(data[0])):
        if (i == 0):
            columns.append("Class")
        else:
            columns.append("Feature " + str(i))
    print(f"columns: {columns}")

def scatterplot(featurelist, datadf):
    pass

print("Here is the scatterplot graphing program.")
newdata = []
x = 0
while (x < 1):
    x = input("Please enter the x value you want to plot: ")
    if (x < 1):
        print("Invalid input!")
y = 0
while (y < 1 or y == x):
    y = input("Please enter the y value you want to plot: ")
    if (y < 1 or y == x):
        print("Invalid input!")
data = promptdataset()
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt') 
        if (x >= len(newdata[0]) or y >= len(newdata[0])):
            print(f"Feature list can not be used with the small test dataset")
        else:
           converttodf(newdata) 
    case 2:
        newdata = normalize('data/large-test-dataset.txt')
        for i in range(len(featurelist)):
            if (x >= len(newdata[0]) or y >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the large test dataset")
        else:
            converttodf(newdata)
    case 3:
        newdata = normalize('data/titanic-clean.txt') 
        for i in range(len(featurelist)):
            if (x >= len(newdata[0]) or y >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the small test dataset")
        else:
            converttodf(newdata)
    case 4:
        custom = 'data/' + input("Please type the name of the file to test: ")
        newdata = normalize(custom) 
        for i in range(len(featurelist)):
            if (x >= len(newdata[0]) or y >= len(newdata[0])):
                badval = True
        if (numfeatures > len(newdata) or badval):
            print(f"Feature list can not be used with the custom dataset")
        else:
            converttodf(newdata)
    case default:
        print("Invalid input!")

