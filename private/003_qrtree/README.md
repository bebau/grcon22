# QRTree

## Solution

### Find the Hideout

* 100 points.
* Topic: Data Science, Machine Learning
* `Flag{(-27.113, -109.350)}`
* Hint for 3 points: *The length of the this binary classification output looks familiar...*
* Hint for 17 points: *The length seems to be semiprime...*

## Explanation

QR Code reveals gort's hideout. Since the QR has 30% error correction, a medium accuracy classifier can still find the solution.

## Generating the Data

### Dependencies

* `apt install qrencode`
* `pip install pandas sklearn pillow umap-learn`