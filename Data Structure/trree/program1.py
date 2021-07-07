# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:07:23 2021

@author: ROHAN
"""

class BST:
    def __init__(self,key):
        self.key=key
        self.lchield=None
        self.rchield=None
root=BST(10)      

root.lchield=BST(5)
print(root.key)  
print(root.rchield)
print(root.lchield.key)