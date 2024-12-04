import pandas as pd
from queue import PriorityQueue
import numpy as np

class Validator:
    def __init__(self, features, classifier, dataset):
        self.features = features
        self.classifier = classifier
        self.dataset = dataset