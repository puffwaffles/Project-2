from queue import PriorityQueue
import numpy as np

#Generate random values for forward selection
def generateforwardval():
    np.random.seed()
    #Mutliply decimal in range (0-1) by 100 to get percentage and round percentages to the tenth's place
    #Multiply by -1 to ensure larger percentages get higher priority
    num = round(np.random.rand() * 100, 1) * -1
    return num

#Checks if a list already exists in the dictionary
def alreadyexists(currlist, usedlists):
    exists = False
    tuplelist = (*currlist, )
    if (currlist in usedlists):
        exists = True
    return exists
    


def forwardselect(numfeatures):
    #Generate random value for no features
    initial = generateforwardval()
    print()
    print(f"Using no features and \"random\" evaluation, I get an accuracy of {initial * -1}%")
    '''#Use priority queue to order feature sets by highest percentage
    pq = PriorityQueue()'''
    #Stores feature lists that were already examined. 
    usedfeaturelists = {} 
    #Create list of features
    fulllist = np.arange(1, numfeatures + 1, 1)
    print("Beginning search.")
    #Store feature list with best accuracy
    bestlist = []
    #Store best accuracy
    bestacc = 0.0
    #Check if accuracy decreases or we encountered the full list
    stop = False
    '''
    while (stop == False):

    for i in range(numfeatures):
        num = generateforwardval()
        print(f"({num}, {i})")
        pq.put((num, i))
    while (pq.empty() == False):
        print(f"{pq.get()[0] * -1}%")'''