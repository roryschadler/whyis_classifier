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
from rdflib.namespace import SKOS

class Classifier(autonomic.GlobalChangeService):
    activity_class = whyis.Classifier

    def getInputClass(self):
        return sio.Entity

    def getOutputClass(self):
        return sio.Entity

    def get_query(self):
        query = '''SELECT ?s WHERE {
    {?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.nanopub.org/nschema#Nanopublication> .}
    UNION { ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://semanticscience.org/resource/UnitOfMeasurement> . }
}'''
        return query

    def process(self, i, o):
        with open("/apps/whyis/agents/whyis_classifier/whyis_classifier/out.txt", "a") as f:
            f.write(i.identifier)
        o.add(SKOS.notation, Literal("rory"))
        new_labels_categories = []
        for name, classifier in user_classifiers:
            new_labels_categories.extend(classifier.label(i))
        for label, category in new_labels_categories:
            o.add(SKOS.notation, Literal(label, datatype=category))
