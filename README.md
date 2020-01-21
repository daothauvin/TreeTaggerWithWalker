# Comparing John Walker’s 18th century grammatical categories against those of today with Treetagger

In this github project you will find every **data** obtained and used in this study.


## Brown

Parts of Brown used in our training and testing of our tagger contained respectively in the directories **TrainingData** and **TestData**.
We also have a file containing the tags that appear in the test and training data in the file **tags-brown**.

## Walker

The part used from Walker in our tests.

## Codes

Python programs created for different purposes :
- [compare.py](Codes/compare.py) : compare differences of tags between two files (with same words)
- [count.py](Codes/count.py) : count tags in a file
- [fusion.py](Codes/fusion.py) : fuse two files line by line with a tabulation between each two lines
- [lexicon.py](Codes/lexicon.py) : define a lexicon with brown corpus data
- [mapfinal.py](Codes/mapfinal.py) : transform tags from brown to tags from Walker's dictionnary ( tags have been transformed to be compatible to TreeTagger )
- [mapspace.py](Codes/mapspace.py) : transform tags from Walker's dictionnary to tags compatible to TreeTagger
- [removeDuplicate.py](Codes/removeDuplicate.py) : remove duplicate lines
- [removeMultiple.py](Codes/removeMultiple.py) : merge lines with same words
- [separateur.py](Codes/separateur.py) : collect texts between a specific XML balise ( <balise> <\\balise> form )
- [tagset.py](Codes/tagset.py) : define a tag set with brown corpus data

## Results

Most of the repertories inside **Results** are split in two repertories **brown** and **walker** that separate information about the two taggers trained with respectively brown tags and walker tags.

### Lexicon

Lexicon for the two taggers, inside **Walker** repertory, you can find two other files that are part of the lexicon : the part coming from Walker's dictionnary **WalkerWords** and words added from brown corpus to complete tag set **addedFromBrownToWalker**

### TagSet

Tag set for the two taggers

### TestAccuracy

Contains :
- files used to compare accuracy
  - **FileToTag-Brown** : text comming from Brown Corpus used to test the taggers
  - **FileToTag-Walker** : text comming from Walker's dictionnary used to test the taggers
- The two **brown** and **walker** repertories are split in two repertories :
  - **TestingWithBrownCorpus** : results of test on **FileToTag-Walker** file
  - **TestingWithWalkerCorpus** : results of test on **FileToTag-Walker** file

  **TestingWithBrownCorpus** contains :

  - **TaggingFromBrown** : the tagging of the test file given by the brown corpus
  - **TaggingResult** : the result file obtained by given the test file to our tagger
  - **counting-TaggingFromBrown** : counting tag of **TaggingFromBrown** file
  - **counting-TaggingResult** : counting tag of **TaggingResult** file
  - **differences-TaggingFromBrown-TaggingResult** : differences obtained between the two results

  **TestingWithWalker** contains :
  - **TaggingResult** : the result file obtained by given the test file to our tagger


### Training

Training data and the count of tags in those.

### TreeTaggerTrainingResult

Taggers optained with our training with brown and Walker's tags.
