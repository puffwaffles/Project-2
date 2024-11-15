# Create node object
class Node:
    # Initilaize node object with list of features and accuracy
    def _init_(self, featurelist, accuracy):
        self.featurelist = featurelist
        self.accuracy = accuracy
    # Returns the list of features
    def getlist(self):
        return self.featurelist
    # Returns the accuracy
    def getacc(self):
        return self.accuracy