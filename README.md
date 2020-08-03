# whyis_classifier

## Installation
- install [whyis](http://tetherless-world.github.io/whyis/install) using this command
  ```
  WHYIS_BRANCH=master bash < <(curl -skL https://raw.githubusercontent.com/tetherless-world/whyis/master/install.sh)
  ```
- whyis will be installed in /apps/whyis

- In your knowledge graph directory, add the classifier agent to the list of inferencers in your config.py file:
  * Add the following import line: `import whyis_classifier.classifier_agent as cl`
  * Add the following line to the `inferencers` item in the `Config` dictionary constructor: `"Classifier": cl.Classifier()`

- Reload your knowledge graph to run the inferencer over it
