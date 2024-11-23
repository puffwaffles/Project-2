from queue import PriorityQueue
import node 
import numpy as np
from listfuncs import*

#Generate random values for backward selection
def generatebackwardval():
    np.random.seed()
    #Mutliply decimal in range (0-1) by 100 to get percentage and round percentages to the tenth's place
    #Multiply by -1 to ensure larger percentages get higher priority
    num = round(np.random.rand() * 100, 1) * -1
    return num

def backwardselect(numfeatures):
    #Generate random value for all features
    initial = generatebackwardval()
    print()
    print(f"Using all features and \"random\" evaluation, I get an accuracy of {initial * -1}%")
    #Use priority queue to order feature sets by highest percentage
    pq = PriorityQueue()
    #Create list of features
    fulllist = np.arange(1, numfeatures + 1, 1)
    #Let's add the all features state to pq
    pq.put((initial, fulllist)) 
    #Stores feature lists that were already examined. 
    usedfeaturelists = {} 
    #Create an entry for all features
    state = {
        "featurelist": (*fulllist, ),
        "parent": None,
        "accuracy": initial * -1 
    }
    #Store node for all features in used features list
    usedfeaturelists.update({state.get("featurelist"): state})
    #Store list of features that can be removed
    currlist = fulllist.copy()
    #Remove list for feature to be removed 
    removed = []
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
        #Check each additional feature combined with curr's feature
        #Use to keep track of previous bestacc
        prevacc = bestacc
        if (curr.getacc() > prevacc):
            #Update best accuracy
            bestacc = curr.getacc()
            #Update best list
            bestlist = curr.getlist()
        # If we reach the empty list, exit
        if (np.array_equal(currlist, [])):
            print(f"Reached empty list!")
            stop = False
            break
        # Say feature set {...} was the best if curr has features
        if (len(removed) > 0):
            if (prevacc < bestacc):
                print(f"Removing feature {removed[0]} increased accuracy the most, changed accuracy to {curr.getacc()}%")
            else:
                print(f"Feature {removed[0]} was the least useful, changed accuracy to {curr.getacc()}%")
        #Update previous node to curr
        prev = curr
        #Add curr's new features to current list and sort it
        currlist = curr.getlist().copy()
        #Sort this list
        currlist.sort()
        #Use remain to store features that can be removed
        remain = currlist.copy()
        #Clear pq
        pq = PriorityQueue()
        #Iterate through remaining features
        for i in range(len(remain)):
            #Use a currchild list to represent each added feature combo
            currchildlist = currlist.copy()
            #Convert currchildlist into list
            currchildlist.tolist()
            #Append new feature to current child list
            currchildlist = np.delete(currchildlist, np.where(currchildlist == remain[i]))
            #Set elements to int
            currchildlist = np.array(currchildlist).astype(int)
            #Sort child list
            currchildlist.sort()
            #If child list is empty, set currlist to empty child list so we can stop at the final iteration
            if (np.array_equal(currchildlist, [])):
                currlist = currchildlist.copy()
            #Check if we already visited this child. If we did not, calculate accuracy and update info
            if (alreadyexists(currchildlist, usedfeaturelists) == False):
                #Calculate accuracy for child    
                childacc = generatebackwardval()
                if (np.array_equal(currchildlist, [])) :
                    print(f"\tUsing no features, I get an accuracy of {childacc * -1}%")
                else:
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
        #Used removed
        removed = remaining(newfront[1], currlist)
        print()
        #Check if we are looking at prev's child node. If we are not, exit 
        if (newfront[0] * -1 < bestacc):
            print("Warning, no significant improvement in accuracy!")
    print(f"Finished search!! The best feature subset is {bestlist}, which has an accuracy of {bestacc}%")            
            
