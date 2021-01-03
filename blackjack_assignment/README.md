# [Blackjack Assignment][1]

The assignment is to construct a basic game of blackjack that allows the 
user to play indefinitely.

The task is an excellent yet simple project requiring the application 
fundamental software engineering concepts.

Click for the full [Assignment Descriptor].


## Dependencies
* Python version: `3.9.0` <sup>1</sup>


## Start up instructions
1. Set your python version to `>=3.9.0` <sup>2</sup>
2. Create & source a venv
```bash
python -m venv .venv_blackjack
source .venv_blackjack/bin/activate
```
3. Run [`blackjack.py`](blackjack.py) script.
- You should see a welcome message and the opening hands for both 
 player/dealer.
- You will then be prompted to hit or stick with numerical options.


## Project structure
- [`blackjack.py`](blackjack.py) is the entry file for the project.
- `README.md` The document you are reading.
- [`Assignment Material/`](Assignment%20Material) contains information and 
reference material provided initially.
- [`components/`](components) contains logical separation of component 
  entities.


## Disclaimer
This is a work in progress and so all issues have been highlighted with 
`TODOs` and `FIXMEs` etc.


## Footnotes
<sup>1</sup> This is to take advantage of "Generic type annotations" that 
are optional but are clear and thus used extensively.</br>
<sup>2</sup> Unfortunately one of the downsides to python is that, beyond 
version 2.x.x & 3.x.x, effective version management requires a 3rd party 
tool (E.g. pyenv, pipenv or docker) to manage available python interpreters. 
Personally, I've chosen to use pyenv here simply because it is a simple tool 
that does one job particularly well and, it enables me to iterate rapidly on 
ideas.


[1]: https://en.wikipedia.org/wiki/Blackjack "Blackjack Wiki"
[Assignment Descriptor]: Assignment%20Material/Assignment%202%20-%20Descriptor.pdf

