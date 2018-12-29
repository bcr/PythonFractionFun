# Overview

```Python
"""
    Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.

    Legal operators shall be *, /, +, - (multiply, divide, add, subtract).

    Operands and operators shall be separated by one or more spaces.

    Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4".

    Improper fractions and whole numbers are also allowed as operands.

    Example run
    ? 1/2 * 3_3/4
    = 1_7/8

    ? 2_3/8 + 9/8
    = 3_1/2
"""
```

## Running from the command line

`python fractionfun.py` will give you a prompt and you can type stuff.

## Running behave

Running the command `behave` will do something interesting. If you don't have `behave` then see the section Installing behave.

Note that running `behave` will pick a random Python to run with. I added `runbehave.py` so that you can run it with any Python you want. On my machine I do `python2 runbehave.py` and `python3 runbehave.py` to run with Python 2 and Python 3.

## Running unit tests

Running `test.py` with your Python of choice will run the unit tests.

## Installing behave

`pip3 install behave` worked for me, but you can consult the [behave docs](https://behave.readthedocs.io/en/latest/) if you want to understand more.