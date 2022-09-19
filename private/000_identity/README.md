# Find the Identity

Classify the sounds to reveal the identity of the outlaw!


Run a classifier on identity.csv to uncover the name of the outlaw. 

The outlaw's name is (Word 1, pos 1) + (Word 2, pos 2) + (Word 3, pos 1) + (Word 4, pos 6).


Getting started
* Uses part of the Marine Mammal Dataset on Kaggle (https://www.kaggle.com/datasets/shreyj1729/best-of-watkins-marine-mammal-sound-database)
* Download the dataset: `kaggle datasets download -d shreyj1729/best-of-watkins-marine-mammal-sound-database` (~7gb, possible to download part of it?)
* Set DATA_PATH to the local data folder in 00_generate_dataset.py

## Dependencies
* `pip install librosa sklearn pandas`

## Solutions

### Flag 1 for XX points

**Flag{gort}**
**g**rayseal
c**o**mmondolphin
**r**ibbonseal
atlan**t**icspotteddolphin


### Bonus points for performance
* Above 90% test accuracy on data_test.csv
* Above 80% test accuracy on data_test.csv

### Hint for XX points

*Our outlaw is also a good swimmer...*