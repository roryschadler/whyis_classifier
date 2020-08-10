from .whyisclassifier import WhyisClassifier
from random import random as rand
from rdflib import URIRef

class TestClassifier(WhyisClassifier):
    def label(self, sample):
        if "http://semanticscience.org/resource/UnitOfMeasurement" in list(sample.objects(subject=None, predicate="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")):
            return "http://nanomine.org/ns/UnitOfMeasurement"
        else:
            return URIRef("http://nanomine.org/ns/NotUnitOfMeasurement")
