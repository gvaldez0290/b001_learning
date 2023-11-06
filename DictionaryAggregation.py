# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:02:08 2023

@author: gvald
https://www.youtube.com/shorts/h1eXDDO_DT8
"""
cart = {
    'cabbage': 2,
    'eggs': 12
}

picnicinv = {
    'butter': 1,
    'cabbage': 1,
    'soda' : 6,
    'turkey' : 34
}

# combine these lists. Sum the duplicates
new_inv = {
    k: cart.get(k,0) + picnicinv.get(k, 0) \
        for k in set(cart | picnicinv)
    }
    
print(new_inv)
