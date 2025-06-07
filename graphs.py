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
import matplotlib.pyplot as plt

def converttodf(data):
    columns = []
    for i in range(len(data[0])):
        if (i == 0):
            columns.append("Class")
        else:
            columns.append("Feature " + str(i))
    df = pd.DataFrame(data, columns = columns)
    print(f"rows: {df.shape[0]}")
    print(f"columns: {df.shape[1]}")
    return df

def scatterplot(x, y, datadf):
    if (y == 0):
        yvalues = np.zeros((datadf.shape[0], ), dtype = int)
        ydf = pd.DataFrame(yvalues, columns = [''])
        yval = ydf.iloc[:, 0]
        xtitle = datadf.columns[x]
        xval = datadf.iloc[:, x]
        print(yval.shape)
        print(xval.shape)
        classvalues = {}
        amount = 0
        mode = ''
        #Iterate through class values to find them 
        for i in range(len(datadf.columns[0])):
            #If we have not found this class value yet, add the vlaue to the map 
            if (datadf.iloc[i][0] not in classvalues):
                classvalues.update({datadf.iloc[i][0]: 1})
            #Otherwise, increment the instances of the value
            else:
                classvalues.update({datadf.iloc[i][0]: classvalues.get(datadf.iloc[i][0]) + 1})
        #Find the total amount of instances of the most common class
        for j in classvalues:
            if (classvalues[j] > amount):
                amount = classvalues[j]
                mode = j
        color = np.where(datadf[datadf.columns[0]] == mode, 'red', 'green')
        plt.scatter(x = xval, y = yval, c = color)
        plt.xlabel(xtitle)
        plt.show()
    else: 
        xtitle = datadf.columns[x]
        ytitle = datadf.columns[y]
        xval = datadf.iloc[:, x]
        yval = datadf.iloc[:, y]
        classvalues = {}
        amount = 0
        mode = ''
        #Iterate through class values to find them 
        for i in range(len(datadf.columns[0])):
            #If we have not found this class value yet, add the vlaue to the map 
            if (datadf.iloc[i][0] not in classvalues):
                classvalues.update({datadf.iloc[i][0]: 1})
            #Otherwise, increment the instances of the value
            else:
                classvalues.update({datadf.iloc[i][0]: classvalues.get(datadf.iloc[i][0]) + 1})
        #Find the total amount of instances of the most common class
        for j in classvalues:
            if (classvalues[j] > amount):
                amount = classvalues[j]
                mode = j
        color = np.where(datadf[datadf.columns[0]] == mode, 'red', 'green')
        plt.scatter(x = xval, y = yval, c = color)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.show()

print("Here is the scatterplot graphing program.")
newdata = []
x = 0
while (x < 1):
    x = int(input("Please enter the x value you want to plot: "))
    if (x < 1):
        print("Invalid input!")
y = -1
while (y < 0 or y == x):
    print("If you don't want to plot against another feature, enter 0 for the value of y")
    y = int(input("Please enter the y value you want to plot: "))
    if (y < 0 or y == x):
        print("Invalid input!")
data = promptdataset()
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt', 1) 
        if (x >= len(newdata[0]) or y >= len(newdata[0])):
            print(f"Feature list can not be used with the small test dataset")
        else:
            newdf = converttodf(newdata)
            scatterplot(x, y, newdf)
    case 2:
        newdata = normalize('data/large-test-dataset.txt', 1)
        if (x >= len(newdata[0]) or y >= len(newdata[0])):
            print(f"Feature list can not be used with the large test dataset")
        else:
            newdf = converttodf(newdata)
            scatterplot(x, y, newdf) 
    case 3:
        newdata = normalize('data/titanic-clean.txt', 1) 
        if (x >= len(newdata[0]) or y >= len(newdata[0])):
            print(f"Feature list can not be used with the titanic test dataset")
        else:
            newdf = converttodf(newdata)
            scatterplot(x, y, newdf)
    case 4:
        custom = 'data/' + input("Please type the name of the file to test: ")
        if (custom.find(".csv") != -1):
            newdata = normalize(custom, 2)
        else:
             newdata = normalize(custom, 1)

        if (x >= len(newdata[0]) or y >= len(newdata[0])):
            print(f"Feature list can not be used with the custom dataset")
        else:
            newdf = converttodf(newdata)
            scatterplot(x, y, newdf)
            
    case default:
        print("Invalid input!")

