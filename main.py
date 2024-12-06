#Group: Katelyn Poon-kpoon015-Wednesday-2PM
#Small Dataset Results:
#Forward: Feature Subset: {3, 5}, Acc: 92.0%
#Backward: Feature Subset: {3, 5}, Acc: 92.0%
#Large Dataset Results:
#Forward: Feature Subset: {1, 27}, Acc: 95.5%
#Backward: Feature Subset: {27}, Acc: 84.7%
#Titanic Dataset Results:
#Forward: Feature Subset: {2}, Acc: 78.0% 
#Backward: Feature Subset: {2}, Acc: 78.0%


from forward import*
from backward import*
from menu import*
from node import*
from listfuncs import*
import pandas as pd

print("Welcome to Katelyn Poon's Feature Selection Algorithm")
features = 0
data = promptdataset()
newdata = []
moveon = False
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt') 
        features = len(newdata[0]) - 1
        moveon = True
    case 2:
        newdata = normalize('data/large-test-dataset.txt')
        features = len(newdata[0]) - 1
        moveon = True
    case 3:
        newdata = normalize('data/titanic-clean.txt') 
        features = len(newdata[0]) - 1
        moveon = True
    case 4:
        custom = 'data/' + input("Please type the name of the file to test: ")
        newdata = normalize(custom) 
        features = len(newdata[0]) - 1
        moveon = True
    case default:
        print("Invalid input!")
if (moveon):
    algorithm = promptalgorithm()
    match algorithm:
        case 1: 
            forwardselect(features, newdata)
        case 2:
            backwardselect(features, newdata)
        case default:
            print("Invalid input!")