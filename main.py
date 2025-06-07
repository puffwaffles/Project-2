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
import sys

print("Welcome to Katelyn Poon's Feature Selection Algorithm")
features = 0
data = promptdataset()
newdata = []
moveon = False
file = ""
match data:
    case 1:
        newdata = normalize('data/small-test-dataset.txt', 1) 
        features = len(newdata[0]) - 1
        moveon = True
        file = "small-test-dataset.csv"

    case 2:
        newdata = normalize('data/large-test-dataset.txt', 1)
        features = len(newdata[0]) - 1
        moveon = True
        file = "large-test-dataset.csv"

    case 3:
        newdata = normalize('data/CS205_small_Data__30.txt', 1) 
        features = len(newdata[0]) - 1
        moveon = True
        file = "CS205_small_Data__30.csv"

    case 4:
        newdata = normalize('data/CS205_large_Data__32.txt', 1)
        features = len(newdata[0]) - 1
        moveon = True
        file = "CS205_large_Data__32.csv"

    case 5:
        newdata = normalize('data/titanic-clean.txt', 1) 
        features = len(newdata[0]) - 1
        moveon = True
        file = "titanic-clean.csv"

    case 6:
        newdata = normalize('data/data.csv', 2) 
        features = len(newdata[0]) - 1
        moveon = True
        file = "data.csv"

    case 7:
        val = input("Please type the name of the file to test: ")
        custom = 'data/' + val
        
        if (custom.find(".csv") != -1):
            newdata = normalize(custom, 2)
            file = val
        else:
            newdata = normalize(custom, 1)
            file = val[:-3] + "csv"
        features = len(newdata[0]) - 1
        moveon = True

    case default:
        print("Invalid input!")

if (moveon):
    algorithm = promptalgorithm()
    match algorithm:
        case 1: 
            fullfile = "accuracy/forward/forward accuracy " + file
            with open(fullfile, "a") as f:
                f.write(f"Features, Accuracy\n")
            
            file2 = "accuracy/time/time " + file[:-3] + "txt"
            start = time.time()
            with open(file2, "a") as f:
                f.write(f"Forward pass\n")
                f.write(f"Time started: {start}\n")
            
            forwardselect(features, newdata, fullfile)
            
            end = time.time()
            elapsed = end - start
            with open(file2, "a") as f:
                f.write(f"Time ended: {end}\n")
                if (elapsed >= 60):
                    f.write(f"Time elapsed: {elapsed / 60} minutes\n")
                elif(elapsed >= 3600):
                    f.write(f"Time elapsed: {elapsed / 3600} hours\n")
                else:
                    f.write(f"Time elapsed: {elapsed} seconds\n")

        
        case 2:
            fullfile = "accuracy/backward/backward accuracy " + file
            with open(fullfile, "a") as f:
                f.write(f"Features, Accuracy\n")
            
            file2 = "accuracy/time/time " + file[:-3] + "txt"
            start = time.time()
            with open(file2, "a") as f:
                f.write(f"Backward pass\n")
                f.write(f"Time started: {start}\n")
            
            backwardselect(features, newdata, fullfile)
            
            end = time.time()
            elapsed = end - start
            with open(file2, "a") as f:
                f.write(f"Time ended: {end}\n")
                if (elapsed >= 60):
                    f.write(f"Time elapsed: {elapsed / 60} minutes\n")
                elif(elapsed >= 3600):
                    f.write(f"Time elapsed: {elapsed / 3600} hours\n")
                else:
                    f.write(f"Time elapsed: {elapsed} seconds\n")

        case default:
            print("Invalid input!")