# Comparing John Walker’s 18th century grammatical categories against those of today with Treetagger

In this github project you will find every **data** obtained and used in this study.


## Brown

Parts of the Brown corpus used in our training and testing can be found in the following directories **TrainingData** and **TestData** respectively.
We also have a file containing the tags that appear in the test and training data in the file **tags-brown**.

## Walker

The part that we used from Walker in our tests.

## Codes

Python programs created for different purposes :
- [compare.py](Codes/compare.py) : to compare the differences of tags between two files (with same words).
- [count.py](Codes/count.py) : to count tags in a file.
- [fusion.py](Codes/fusion.py) : to fuse two files line by line with a tabulation between each and every two lines.
- [lexicon.py](Codes/lexicon.py) : to define a lexicon with the Brown corpus data.
- [mapfinal.py](Codes/mapfinal.py) : to transform tags from the Brown corpus data to tags from Walker's dictionary ( tags have been transformed to be compatible with TreeTagger ).
- [mapspace.py](Codes/mapspace.py) : to transform tags from Walker's dictionary to tags compatible to TreeTagger.
- [removeDuplicate.py](Codes/removeDuplicate.py) :to remove duplicate lines.
- [removeMultiple.py](Codes/removeMultiple.py) : to merge lines with the same words.
- [separateur.py](Codes/separateur.py) : to collect texts between a specific XML balise ( <balise> <\\balise> form ).
- [tagset.py](Codes/tagset.py) : to define a tag set with the Brown corpus data.

## Results

Most of the repositories inside **Results** are split into two repositories **brown** and **walker** that separate information about the two taggers trained with the Brown's tags and Walker's tags respectively.

### Lexicon

Lexicon for the two taggers, inside **Walker** repository, you can find two other files that are part of the lexicon : the part coming from Walker's dictionary **WalkerWords** and words added from the Brown corpus to complete the tag set **addedFromBrownToWalker**.

### TagSet

Tag sets for the two taggers.

### TestAccuracy

Contains:
- files used to compare accuracy
  - **FileToTag-Brown** : text coming from the Brown Corpus used to test the taggers.
  - **FileToTag-Walker** : text coming from Walker's dictionary used to test the taggers.
- The two **brown** and **walker** repositories are split in two repositories :
  - **TestingWithBrownCorpus** : test's results on **FileToTag-Walker** file.
  - **TestingWithWalkerCorpus** : test's results on **FileToTag-Walker** file.

  **TestingWithBrownCorpus** contains:

  - **TaggingFromBrown** : the tagging of the test file given by the Brown corpus.
  - **TaggingResult** : the result file obtained by feeding our tagger the test file.
  - **counting-TaggingFromBrown** : **TaggingFromBrown** file's tags and their occurences.
  - **counting-TaggingResult** : **TaggingResult** file's tags and their occurences.
  - **differences-TaggingFromBrown-TaggingResult** : the differences that we got between the two results.

  **TestingWithWalker** contains :
  - **TaggingResult** : the result file obtained by feeding our tagger the test file.


### Training

Training data and its tags with occurences.

### TreeTaggerTrainingResult

Tags obtained by training Brown's and Walker's tags.
