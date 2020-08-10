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

from rdflib.namespace import RDF
from rdflib.term import Node
from .user_classifiers import user_classifiers

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
        labels = []
        for name, classifier in user_classifiers:
            labels.extend(classifier.label(i))

        for new_type in labels:
            if not isinstance(new_type, Node):
                new_type = URIRef(new_type)
            o.add(RDF.type, new_type)
