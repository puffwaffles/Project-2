from forward import*
from backward import*
from menu import*
from node import*

features = promptnumfeatures()
algorithm = promptalgorithm()
match algorithm:
    case 1: 
        forwardselect(features)
    case 2:
        backwardselect(features)
    case default:
        print("Invalid input!")