# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:05:40 2023

@author: gvald

https://www.youtube.com/shorts/32XIgqI3E0I
Merge, filter out duplicates of 2 lists 
"""
def merge_list (arrayA, arrayB):
    return sorted(set(arrayA + arrayB))
a = [2, 9, 6, 2, 8]
b = [12, 6, 74, 9, 12, 5]

c = merge_list(a,b)
print(c)
