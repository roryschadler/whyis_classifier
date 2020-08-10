class WhyisClassifier():
    """ Base class for the Whyis Classifier."""

    def __init__(self):
        pass

    def label(self, sample):
        """ Return a list of labels to be applied to the given sample.
            Can classify the sample based on any attributes of the sample itself.

            labels: a list of labels to add to the knowledge graph.
                Can be a URI string, or an rdflib.URIRef object

                example: ["http://nanomine.org/ns/Elastomer",
                          rdflib.URIRef("http://nanomine.org/ns/TransparentMaterial")]
        """
        labels = []
        return labels
