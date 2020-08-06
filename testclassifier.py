from whyisclassifier import WhyisClassifier
from random import random as rand

class TestClassifier(WhyisClassifier):
    def label(self, sample):
        if rand() < 0.5:
            print("No")
        else:
            print("Yes")
        return []
