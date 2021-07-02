# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:04:17 2020

@author: ASUS
"""
# =============================================================================
# import math
# class Point:
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#     
#     def reset(self):
#         self.move(0, 0)
#     
#     def calculate_distance(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
# 
# point1 = Point()
# point2 = Point()
# 
# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))
# assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
# point1.move(3, 4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))
# =============================================================================
# =============================================================================
# class Point:
#     def __init__(self, x=0, y=0):
#         self.move(x, y)
#     
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#     
#     def reset(self):
#         self.move(0, 0)
# 
# point = Point(3)
# print(point.x, point.y)
# =============================================================================
# =============================================================================
# import math
# 
# class Point:
#     'Represent a point in two-dimensional geometric coordinatees'
#     
#     def __init__(self, x=0, y=0):
#         '''Initialize the position of a new point. The x and y coordinates can be specified.If they are not, 
#         the point defaults to the origin.'''
#         self.move(x, y)
#     
#     def move(self, x, y):
#         "Move the point to a new locationn in 2D space."
#         self.x = x
#         self.y = y
#     
#     def reset(self):
#         'Reset the point back to the geometric origin:0, 0'
#         self.move(0, 0)
#     
#     def calculate_distance(self, other_point):
#         """Calculate the distance from this point to a second point passed as a parameter.
#         This function uses the Pythongorean Theorem to calculate the distance between the two Points.The 
#         distance is returned as a float."""
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
# if __name__ == "__main__":
#     print("我被执行了")
# =============================================================================
# =============================================================================
# def format_string(string, formatter=None):
#     class DefaultFormatter:
#         def format(self, string):
#             return str(string).title()
#     if not formatter:
#         formatter = DefaultFormatter()
#     return formatter.format(string)
# 
# hello_string = "hello world, how are you today?"
# print(" input: " + hello_string)
# print("output: " + format_string(hello_string))
# =============================================================================
class SecretString:
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    
    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ' '