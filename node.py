# https://www.w3schools.com/python/ref_func_sorted.asp
# https://www.geeksforgeeks.org/python-difference-two-lists/
# Create node object
class Node:
    # Initilaize node object with list of features and accuracy
    def _init_(self, parent, featurelist, accuracy):
        self.parent = parent
        self.featurelist = featurelist
        self.accuracy = accuracy
    # Returns the list of features
    def getlist(self):
        return self.featurelist
    # Returns the accuracy
    def getacc(self):
        return self.accuracy
    # Returns the parent node
    def getparent(self):
        return self.parent