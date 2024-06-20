#!/usr/bin/env python
# coding: utf-8

# In a jupyter notebook solve the following question using python. Please upload the notebook to GitHub and provide the link submission box below.
# 
# 
# Develop a recursive function tough() that takes two nonnegative integer arguments and outputs a pattern as shown below. Hint: The first argument represents the indentation of the pattern, where the second argument -- always a pattern of 2 indicates the number *s in the longest line of *s in the pattern

# In[2]:


def tough(indent,length):
    if length== 0:
        return
    if indent > 0:
        print(" " * indent, end='')
    print("*" *length)
    tough(indent+1,length-1)

tough(0,0)
print()
tough(0,1)
print()
tough(0,2)
print()
tough(0,4)
print()

