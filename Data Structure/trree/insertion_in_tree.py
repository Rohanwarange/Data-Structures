# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:44:08 2021

@author: ROHAN
"""

class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.key==None:
           self.key=key
           return
        if self.key>=key:
           if self.lchild:
              self.lchild.insert(key)
           else:
               self.lchild=BST(key)
        else:
           if self.rchild:
              self.rchild.insert(key)
           else:    
              self.rchild=BST(key)
tree=BST(None)              
#tree.insert(20)
l=[10,20,54,89,85,00,22,56,55,85,22,856,186,254652,545,85,1]
for i in l:
    tree.insert(i)
    print(tree.key)