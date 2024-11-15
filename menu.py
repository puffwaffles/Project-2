def promptnumfeatures():
    numfeatures = 0
    numfeatures = int(input("Please enter total number of features: "))
    while (numfeatures <= 0): 
        print("Invalid input for feature choice!")
        numfeatures = int(input("Please enter total number of features: "))
    return numfeatures

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