import unittest
from functools import partial

def fullname(first, second):
  return first + " " + second

assert fullname("John", "Doe") == "John Doe"
assert fullname("","") == " "
assert partial(fullname, "John")("Doe") == "John Doe"