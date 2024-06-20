#!/usr/bin/env python
# coding: utf-8

# # Quistion-21
# 
# In a jupyter notebook solve the following question. Please upload the notebook to GitHub and provide the link submission box below.
# 
#  
# 
# __int()__: Constructor that takes as input a pair of Point objects that represent the ends points of the line segment
# 
# Length():: returns the length if the segment 
# 
# Slope() returns the slope of the segment of none if the slope is unbounded 
# 
#  
# 
# >>> p1 = Point(3,4)
# 
# >>> p2 = Point()
# 
# >>> s = Segment(p1,p2)
# 
# >>> s.length()
# 
# 5.0
# 
# >>> s.slope()
# 
# 0.75

# In[39]:


import math

class Point:
    def __init__(self, x=0, y=0): 
        self.x = x
        self.y = y

class Segment:
    def __init__(self, p1, p2): 
        self.p1 = p1
        self.p2 = p2

    def length(self):
        
        x_coordinates = self.p2.x - self.p1.x
        y_coordinates = self.p2.y - self.p1.y

        distance = math.sqrt(x_coordinates**2 + y_coordinates**2) 

        return distance

    def slope(self):
        try:
            return (self.p2.x - self.p1.x) / (self.p2.y - self.p1.y)
        except ZeroDivisionError: 
            return None
        
       
        p1 = Point(3, 4)
        p2 = Point()
        s = Segment(p1, p2)
        
        
    print(s.length())  

    print(s.slope())  

