import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
apifold = os.path.dirname(parent)
shi = os.path.dirname(apifold)
sys.path.append(shi)
sys.path.append(apifold)

from api.elements.textParsing.classifier import *

classifier = Classifier()

while True:
    d = input("inp: ")
    request_params = classifier.get(0, d)[0]
    print(request_params)