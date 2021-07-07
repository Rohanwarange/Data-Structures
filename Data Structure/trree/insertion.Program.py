# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:03:11 2021

@author: ROHAN
"""

class BST:
    def __init__(self,key):
        self.key=key
        self.lchield=None
        self.rchield=None
        
     #to insert element in tree
    def insert(self,data):
         if self.key is None:
             self.key=data
         else:
             if self.key>data:
                 if self.lchield:
                     self.lchield.insert(data)
                 else:
                     self.lchild=BST(data)
             else:
                  if self.rchield:
                     self.rchield.insert(data)
                  else:
                     self.rchild=BST(data)
root=BST(10)   
root.insert(20)
print(root.key)  
print(root.rchield)
print(root.lchield)