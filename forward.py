from queue import PriorityQueue
import numpy as np

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
    for i in range(numfeatures):
        num = generateforwardval()
        print(f"({num}, {i})")
        pq.put((num, i))
    while (pq.empty() == False):
        print(f"{pq.get()[0] * -1}%")