# Get into the bunker

## Solution

* 41 points.
* Topic: Sudoku
* `Flag{ReD2uM}`
* A neat hexadecimal puzzle. I solved this by hand but I suspect folks will use an online-solver, making it pretty easy.

## Explanation

![solution hexadoku](hexadoku_private_sm.svg)

```python
''.join([chr(x) for x in [0x52, 0x65, 0x44, 0x32, 0x75, 0x4d]])
```

## Generator

* [Hexadoku Generator](https://www.sudoku-puzzles-online.com/hexadoku/enter-a-solution-hexadoku-solution.php)
* Confirmed puzzle # 798

## Encoded Grid

```
*  *  E  9   *  *  6  *   *  F  *  *   2  *  7  *
*  *  5  2   C  7  *  *   D  9  *  *   *  B  *  *
*  F  *  *   *  *  *  *   *  *  *  C   *  *  *  *
A  *  *  *   *  8  *  5   E  *  3  *   F  D  *  *

*  *  3  *   5  2  4  *   A  *  7  *   *  C  *  1
C  *  *  A   *  6  9  *   *  D  *  *   *  *  *  *
*  E  F  *   *  *  *  *   9  *  *  8   *  *  *  *
B  *  D  *   F  *  E  8   *  *  *  *   *  *  *  7

*  *  1  7   *  *  *  E   *  *  D  *   0  F  *  *
*  B  8  F   4  *  *  *   *  *  *  A   D  *  6  *
2  *  *  *   9  F  *  *   6  5  *  1   *  3  *  *
E  9  *  *   B  *  *  *   *  *  C  7   *  8  A  *

*  *  *  C   3  9  D  *   *  *  *  F   *  6  *  8
6  *  *  *   *  *  *  1   *  E  *  *   7  *  D  A
7  8  A  *   *  *  *  *   *  *  *  *   *  *  *  *
*  *  4  *   *  *  *  7   C  B  *  *   5  2  *  *
```

344a7644de5ff9444512983d9fc6a122
