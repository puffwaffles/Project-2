from queue import PriorityQueue
import node 
import numpy as np
from listfuncs import*

#Generate random values for forward selection
def generateforwardval():
    np.random.seed()
    #Mutliply decimal in range (0-1) by 100 to get percentage and round percentages to the tenth's place
    #Multiply by -1 to ensure larger percentages get higher priority
    num = round(np.random.rand() * 100, 1) * -1
    return num

def forwardselect(numfeatures):
    #Generate random value for no features
    initial = generateforwardval()
    print()
    print(f"Using no features and \"random\" evaluation, I get an accuracy of {initial * -1}%")
    #Use priority queue to order feature sets by highest percentage
    pq = PriorityQueue()
    #Let's add the no features state to pq
    pq.put((initial, [])) 
    #Stores feature lists that were already examined. 
    usedfeaturelists = {} 
    #Create an entry for no features
    state = {
        "featurelist": (*[], ),
        "parent": None,
        "accuracy": initial * -1 
    }
    #Store node for no features in used features list
    usedfeaturelists.update({state.get("featurelist"): state})
    #Create list of features
    fulllist = np.arange(1, numfeatures + 1, 1)
    #Store list of already gathered features
    currlist = []
    print("Beginning search.")
    #Store feature list with best accuracy
    bestlist = []
    #Store best accuracy
    bestacc = 0.0
    #Check if accuracy decreases or we encountered the full list
    stop = False 
    #Create previous node
    prev = None 
    while (stop == False):
        #Aquire front of pq
        front = pq.get()
        # Get curr from the front of pq
        curr = node.Node(prev, front[1], front[0] * -1)
        # If curr's accuracy is worse/same as best acc, stop 
        if (np.array_equal(curr.getlist(), fulllist)):
            if (curr.getacc() < bestacc):
                print("Warning, Accuracy has decreased!")
            elif (curr.getacc() == bestacc):
                print("Warning, Accuracy has not improved!")
            print(f"Reached full list!")
            print()
            stop = True
            break
        if (curr.getacc() < bestacc):
            print("Warning, Accuracy has decreased!")
            print(f"Feature set {curr.getlist()} was the best out of the group, accuracy is {curr.getacc()}%")
        elif (curr.getacc() == bestacc):
            print("Warning, Accuracy has not improved!")
            print(f"Feature set {curr.getlist()} was the best out of the group, accuracy is {curr.getacc()}%")
        # Otherwise, check each additional feature combined with curr's feature
        else :
            #Update best accuracy
            bestacc = curr.getacc()
            #Update best list
            bestlist = curr.getlist()
            # If we reach the full list, exit
            # Say feature set {...} was the best if curr has features
            if (len(curr.getlist()) > 0):
                print(f"Feature set {curr.getlist()} was the best, accuracy is {curr.getacc()}%")
        #Update previous node to curr
        prev = curr
        #Add curr's new features to current list and sort it
        currlist.extend(remaining(currlist, curr.getlist()))
        #Sort this list
        currlist.sort()
        #Update list of remaining features
        remain = remaining(currlist, fulllist)
        #Sort this list
        remain.sort()
        #Reset pq
        pq = PriorityQueue()
        #Iterate through remaining features
        for i in range(len(remain)):
            #Use a currchild list to represent each added feature combo
            currchildlist = currlist.copy()
            #Append new feature to current child list
            currchildlist.append(remain[i])
            #Set elements to int
            currchildlist = np.array(currchildlist).astype(int)
            #Sort child list
            currchildlist.sort()
            #Check if we already visited this child. If we did not, calculate accuracy and update info
            if (alreadyexists(currchildlist, usedfeaturelists) == False):
                #Calculate accuracy for child    
                childacc = generateforwardval()
                print(f"\tUsing feature(s) {currchildlist}, I get an accuracy of {childacc * -1}%")
                #Add new state to pq
                pq.put((childacc, currchildlist))
                #Create an entry for new combo
                newstate = {
                    "featurelist": (*currchildlist, ),
                    "parent": prev,
                    "accuracy": childacc * -1 
                }
                #Store node for no features in used features list
                usedfeaturelists.update({newstate.get("featurelist"): newstate})
        #Aquire new front of pq
        newfront = pq.get()
        #Put it back for next iteration
        pq.put((newfront[0], newfront[1]))
        print()
    print(f"Finished search!! The best feature subset is {bestlist}, which has an accuracy of {bestacc}%")            
            