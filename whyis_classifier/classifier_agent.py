""" Classification Agent for Whyis
    Uses <http://tetherless-world.github.io/whyis/inference>
    as a template.
"""

from __future__ import division
from past.utils import old_div
import nltk, re, pprint
from rdflib import *
from rdflib.resource import Resource
import logging


from whyis import autonomic
from whyis import nanopub
from whyis.namespace import sioc_types, sioc, sio, dc, prov, whyis

from rdflib.namespace import RDF
from rdflib.term import Node
from .user_classifiers import user_classifiers

class Classifier(autonomic.GlobalChangeService):
    activity_class = URIRef("http://nanomine.org/ns/WhyisClassifierV001")

    def getInputClass(self):
        return sio.Entity

    def getOutputClass(self):
        return sio.Entity

    def get_query(self):
        query = '''SELECT ?s WHERE {
    ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://nanomine.org/ns/PolymerNanocomposite> .
}'''
        return query

    # mostly copied from superclass whyis.autonomic.Service
    def process_graph(self, inputGraph):
        # repeat processing for every user classifier
        for name, classifier in user_classifiers:
            instances = self.getInstances(inputGraph)
            results = []
            for i in instances:
                print("Processing", i.identifier, self)
                output_nanopub = self.app.nanopub_manager.new()
                o = output_nanopub.assertion.resource(i.identifier)  # OutputClass(i.identifier)
                error = False
                try:
                    label, confidence = classifier.label(i)
                    if not isinstance(label, Node):
                        label = URIRef(label)
                    o.add(RDF.type, label)
                    output_nanopub.provenance.add(
                        (output_nanopub.assertion.identifier, sio.ProbabilityMeasure, Literal(confidence)))
                except Exception as e:
                    output_nanopub.add(
                        (output_nanopub.assertion.identifier, self.app.NS.sioc.content, Literal(str(e))))
                    logging.exception("Error processing resource %s in nanopub %s" % (i.identifier, inputGraph.identifier))
                    error = True
                for new_np in self.app.nanopub_manager.prepare(ConjunctiveGraph(store=output_nanopub.store)):
                    if len(new_np.assertion) == 0 and not error:
                        continue
                    self.explain(new_np, i, o, classifier.identifier)
                    new_np.add((new_np.identifier, sio.isAbout, i.identifier))
                    # print new_np.serialize(format="trig")
                    if not self.dry_run:
                        self.app.nanopub_manager.publish(new_np)
                    else:
                        print("Not publishing",new_np.identifier,", dry run.")
                    results.append(new_np)
        return results

    def explain(self, nanopub, i, o, classifier):
        activity = nanopub.provenance.resource(BNode())
        activity.add(RDF.type, self.activity_class)
        activity.add(prov.wasAssociatedWith, classifier)
        nanopub.pubinfo.add((o.identifier, RDF.type, self.getOutputClass()))
        nanopub.provenance.add((nanopub.assertion.identifier, prov.wasGeneratedBy, activity.identifier))
