# GRCon 22

Puzzles & code for GNU Radio conference 2022.

## Notes

All of our challenges are independent, but there is a pseudo story to the flavortext that ties them all together. They could be revealed every few hours or after completion of the one previous. Solving the "wanted" challenge gives a hint to the "qrtree" challenge and vice-versa.

I don't know how many points per challenge is good, but we'll pretend 100 is a base value and suggest a number based on difficulty. Scale as appropriate.

Each challenge has a `public/` folder that holds files facing the challenger, and a `private/` folder with solutions and creation files for the challenge.

## *Solve My Bomb* Challenges

### Flavortext

A rumor comes across your desk: a dangerous terrorist has plans to commit evil deeds. The CIA, FBI, British Secret Intelligence Service, and many more organizations from around the world have invested time, manpower, weapons, and energy into finding him, but he has stealthily evaded capture. No one outside of world intelligence leaders knows who he is or what his intentions are. All your sources are able to tell you is that this mission is a priority for the entire world. Your time has come. 

### `000_identity/`

#### What is the identity of the terrorist?

* 75 points.
* Topic: Data Science / Machine Learning
* `Flag{gort}`
* Hint for 22 points: *Our outlaw is also a good swimmer*

### `001_wanted/`

* Topic: SDR, Trivia

#### What is the bounty on the terrorist's head?

* 125 points.
* `Flag{$198,733}` or `Flag{198733}` or `Flag{198,733}`
* Hint for 23 points: *777 samples per symbol*
* Hint for 33 points: *Bounty is outside the HAM bandplan*

#### Bonus: What band composed the cat piano melody?

* 25 points.
* `Flag{Radiohead}`

### `003_qrtree/`

#### Where is the terrorist?

* 100 points.
* Topic: Data Science, Machine Learning
* `Flag{(-27.113, -109.350)}`
* Hint for 3 points: *The length of the this binary classification output looks familiar...*
* Hint for 17 points: *The length seems to be semiprime...* 

### `004_hexadoku/`

#### How to get into the bunker?

* 41 points.
* Topic: Sudoku
* A neat hexadecimal puzzle. I solved this by hand but I suspect folks will use an online-solver, making it pretty easy.

### `002_bomb/`

Despite the numbering, this is the last challenge. A decompiling challenge.

#### What is the username?

* 100 points.
* Topic: Reverse Engineering
* `Flag{}`
* Hint for X points: *I bet the terrorist has a loophole built in in case he forgets his password. He is a software mastermind, but he hasn't picked the most secure python functionality. Let's try entering { as a password and see if there's a possible vulnerability to exploit.*
* Hint for Y points: *As a hacker, you know you can inspect python bytecode with a certain method from the Python documentation. Then you can get names of variables, constants, attributes, etc.*

