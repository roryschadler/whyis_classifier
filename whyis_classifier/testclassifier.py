from .whyisclassifier import WhyisClassifier
from random import random as rand

class TestClassifier(WhyisClassifier):
    def label(self, sample):
        if "http://semanticscience.org/resource/UnitOfMeasurement" in list(sample.objects(subject=None, predicate="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")):
            return [("Unit","http://rory.org/rory")]
        else:
            return [("Not Unit","http://rory.org/rory")]
