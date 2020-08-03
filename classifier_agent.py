""" Classification Agent for Whyis
    Uses <http://tetherless-world.github.io/whyis/inference>
    as a template.
"""

from __future__ import division
from past.utils import old_div
import nltk, re, pprint
from rdflib import *
from rdflib.resource import Resource
from time import time

from whyis import autonomic
from whyis import nanopub
from whyis.namespace import sioc_types, sioc, sio, dc, prov, whyis

from .user_classifiers import user_classifiers
skos = rdflib.namespace("http://www.w3.org/2004/02/skos/core#")

class Classifier(autonomic.GlobalChangeService):
    activity_class = whyis.Classifier

    def getInputClass(self):
        return sio.Entity

    def getOutputClass(self):
        return sio.Entity

    def get_query(self):
        query = '''SELECT ?s WHERE {
    ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://nanomine.org/ns/PolymerNanocomposite> .
}'''
        return query

    def process(self, i, o):
        new_labels_categories = []
        for name, classifier in user_classifiers:
            new_labels_categories.extend(classifier.label(i))

        for label, category in new_labels_categories:
            o.add(skos.notation, Literal(label, datatype=category))
