# Comparing John Walker’s 18th century grammatical categories against those of today with Treetagger

In this github project you will find every **data** obtained  in this study.


## Brown

Parts of Brown used in our training and testing of our tagger respectively in the directories **TrainingData** and **TestData**.
We also give tags that appear in the test and training data in the file **tags-brown**

## Walker

The part used from Walker in our tests

## Codes

Python programs created for different purposes :
- compare.py : compare differences of tags between two files (with same words)
- count.py : count tags in a file
- fusion.py : fuse two files raw by raw with a tabulation between the two raws
- lexicon.py : define a lexicon with brown corpus
- mapfinal.py : transform tags from brown to tags from walker ( tags have been transformed to be compatible to TreeTagger )
- mapspace.py : transform tags from walker to tags compatible to TreeTagger
- removeDuplicate.py : remove duplicate lines
- removeMultiple.py : merge lines with same words
- separateur.py : collect texts between a specific tag
- tagset.py : complete tag set from brown

## Results

Most of the repertories inside **Results** are split in two repertories **brown** and **walker** that separate information about tree tagger with brown tags and walker tags

### Lexicon

Lexicon for the two taggers, inside **Walker** repertory, you can find two other files that are part of the lexicon, the part coming from walker's dictionnary : **WalkerWords** and words added from brown to complete some tags : **addedFromBrownToWalker**

### TagSet

Tag set for the two taggers

### TestAccuracy

Contains :
- files used to compare accuracy
  - **FileToTag-Brown** : text comming from Brown Corpus
  - **FileToTag-Walker** : text comming from Walker's dictionnary
- The two **brown** and **walker** repertories are split in two repertories :
  - **TestingWithBrownCorpus** : results of test on **FileToTag-Walker** file
  - **TestingWithWalkerCorpus** : results of test on **FileToTag-Walker** file

  **TestingWithBrownCorpus** contains :

  - **TaggingFromBrown** : the result from brown
  - **TaggingResult** : the result file obtained by given the test file to our tagger
  - **counting-TaggingFromBrown** : counting tag of **TaggingFromBrown** file
  - counting-TaggingResult : counting tag of **TaggingResult** file
  - **differences-TaggingFromBrown-TaggingResult** : differences obtained between the two results

  **TestingWithWalker** contains :
  - **TaggingResult** : the result file obtained by given the test file to our tagger


### Training

Training data and the count of tags in those

### TreeTaggerTrainingResult

Taggers optained with our training with brown and walker tags.
