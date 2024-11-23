from queue import PriorityQueue
import node 
import numpy as np

#Checks if a list already exists in the dictionary
def alreadyexists(currlist, usedlists):
    exists = False
    tuplelist = (*currlist, )
    if (tuplelist in usedlists):
        exists = True
    return exists
    
#Returns list of unselected features
def remaining(currlist, fulllist):
    remain = []
    if (len(currlist) == 0):
        remain = fulllist.copy()
    else:
        remain = list(set(fulllist) - set(currlist))
    return remain
