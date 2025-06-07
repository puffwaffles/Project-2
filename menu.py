import pandas as pd
import sys
#Prompt user for the number of features
def promptnumfeatures():
    numfeatures = 0
    numfeatures = int(input("Please enter total number of features: "))
    while (numfeatures <= 0): 
        print("Invalid input for feature choice!")
        numfeatures = int(input("Please enter total number of features: "))
    return numfeatures

#Prompt user for list of features
def promptfeatures(numfeatures):
    features = []
    sys.stdout.write("Please enter the list of features: ")
    num = 0
    list1 = []
    #Prompt user for list of values
    while (len(list1) != numfeatures):
        list1 = [i for i in input().split()]
    for i in range(numfeatures):
        features.append(int(list1[i]))
    features.sort()
    print(f"Selected features: {features}")
    return features

#Prompt user for dataset
def promptdataset():
    data = 0
    print()
    print("1. Small Dataset")
    print("2. Large Dataset")
    print("3. Small 30 Dataset")
    print("4. Large 32 Dataset")
    print("5. Titanic Dataset")
    print("6. Soybeans Dataset")
    print("7. Custom Dataset")
    data = int(input("Please type the number of the dataset you want to use: "))
    while (data <= 0 or data > 7): 
        print("Invalid input for algorthim choice!")
        print()
        print("1. Small Dataset")
        print("2. Large Dataset")
        print("3. Small 30 Dataset")
        print("4. Large 32 Dataset")
        print("5. Titanic Dataset")
        print("6. Soybeans Dataset")
        print("7. Custom Dataset")
        data = int(input("Please type the number of the dataset you want to use: "))
    return data

#Prompt user for the algorithm
def promptalgorithm():
    algorithm = 0
    print()
    print("1. Forward Selection")
    print("2. Backward Elimination")
    algorithm = int(input("Please type the number of the algorithm you want to run: "))
    while (algorithm <= 0 or algorithm > 2): 
        print("Invalid input for algorthim choice!")
        print()
        print("1. Forward Selection")
        print("2. Backward Elimination")
        algorithm = int(input("Please type the number of the algorithm you want to run: "))
    return algorithm