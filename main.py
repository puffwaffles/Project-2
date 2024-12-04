from forward import*
from backward import*
from menu import*
from node import*
from listfuncs import*
import pandas as pd

features = promptnumfeatures()
data = promptdataset()
newdata = []
moveon = False
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt') 
        #moveon = True
    case 2:
        newdata = normalize('data/large-test-dataset.txt')
        moveon = True
    case default:
        print("Invalid input!")
if (moveon):
    algorithm = promptalgorithm()
    match algorithm:
        case 1: 
            forwardselect(features)
        case 2:
            backwardselect(features)
        case default:
            print("Invalid input!")