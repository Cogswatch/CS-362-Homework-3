import unittest

# Write code to calculate the volume of a cube
def cube(sideLength):
  return sideLength * sideLength * sideLength

assert cube(10) == 1000
assert cube(0) == 0
assert cube(-10) == -1000