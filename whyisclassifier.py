class WhyisClassifier():
    """ Base class for the Whyis Classifier."""

    def label(self, sample):
        """ Return a list of labels and categories to be applied.

            label_category_tuples: a list of tuples (label, category) to add
                to the knowledge graph

                label: a string to label the graph pattern with
                category: a string giving the URI of the category that label
                    belongs to

                example: [("Elastomer", "http://nanomine.org/ns/PolymerType"),
                          ("Biocompatible", "http://nanomine.org/ns/Category1011"),
                          ("Transparent", "http://nanomine.org/ns/Category3251")]
        """
        label_category_tuples = []
        return label_category_tuples
