## A Python FizzBuzz example

---



This is a (not quite so simple) simple example of the common python developer interview question "FizzBuzz".

Since both, Python as a programming language and the fizzbuzz exercise are rather straight forward, this project is an
attempt at showing how to make a small yet proper Python module. The idea was to use a very simple example to demonstrate
the use of unit tests, argparse, assertions/typechecking, classes, iterators, generators (aka __yield__), using a main method and offereing two ways to run fizzbuzz with
command line arguments. On top of that, it tries to follow a best-practice approach of test-driven development. In other words, write
your tests first!

#### Overview
Generally, for either a single number or a range of numbers, fizzbuzz should print *Fizz* for multiples of 3, print *Buzz*
if x mfor multiples of 5, *FizzBuzz* for multiples of 3 and 5 and the value itself otherwise. In this project you can do that by
either providing a start and end point or a start point only. If you only provide a start value, the iteration will actually start at 1 and end
at the provided value (*see Improvement section*), When providing both, start and end value, fizzbuzz will print for the range in between.
If start and en are the same fizzbuzz print only for that value. If the start value is larger than the end value fizzbuzz will print in decreasing order.

#### Installation
Clone or download and unzip the repo. in the root of the project, you can run the tests with:

`python -m unittest tests/test_fizzbuzz.py`

(*Note: this is assuming Python 3.x*)

There are two ways to run fizzbuzz.

1. Using the python command

You can run the fizzbuzz implementation directly with `python -m fizzbuzz --start= --end= ` or show brief help with
`python -m fizzbuzz -h`.

2. As a command line app

From the root of the project (tested on Linux) you can run `pip install .` (*with the dot at the end*) This will create an executable
python mudole and add `fizzbuzz` to your PATH, which simply makes it available in your command line with `fizzbuzz -h` to see the options.



#### Improvements
 * This project uses the `unittest` module that ships with Python. In many (larger) cases it is preferable to use
the [pytest](https://docs.pytest.org/en/latest/) framework.
 * Change confusing variable naming of start and end, because when only start is provided it is actually the end point and
 iteration starts at on