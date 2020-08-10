# Import your classifier here
from .whyisclassifier import WhyisClassifier
from .testclassifier import TestClassifier

# Add your classifier to this dictionary
user_classifiers = {
    'dummy_classifier': WhyisClassifier(),
    'test_classifier': TestClassifier()
}
