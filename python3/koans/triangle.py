#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # try:
    #     isValid(a, b, c)
    # except TriangleError as ex:
    #     return ex.args[0]

    ### This works because they want the raised excpetion to not be caught
    isValid(a,b,c)

    if(a == b == c):
        return 'equilateral'
    elif(a == b or a == c or b == c):            
        return 'isosceles'
    else:
        return 'scalene'

def isValid(a, b, c):
    if(a | b | c <= 0):
        raise TriangleError("All sides must be greater than 0")

    if(((a+b) < c) or ((a+c) < b) or ((c+b) < a)):
        raise TriangleError("Two sides should be greater than third")

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
