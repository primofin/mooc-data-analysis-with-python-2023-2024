# Enter you module contents here
"""Helper functions for triangles."""

__author__ = "Vy Nguyen"
__version__ = "1"

import math 


def hypotenuse (s1, s2):
  """Computes the length of the hypotenuse of a right-angled triangle
  with sides of length a and b."""
  return math.sqrt(s1**2 + s2**2)

def area (s1, s2):
  """Computes the area of a right-angled triangle
  with sides of length a and b."""
  return (s1 * s2) / 2

