# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:33:21 2021

@author: ROHAN
"""

class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key==None:
           self.key=data
        else:
            if self.key>=data:
               if self.lchild:
                   self.lchild.insert(data)
               else:
                   self.lchild=BST(data)
            else:
                if self.rchild:
                   self.rchild.insert(data)
                else:
                    self.rchild=BST(data)
    def Delete(self,data):
        if self.key is None:
            print("Node is Not Found : :")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.Delete(data)
            else:
                print("Node is Not Found : ")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.Delete(data)
            else:
                print("node is Not Found")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.Delete(data)
            return self
    def preorder(self):
        print(f"{self.key} --->",end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
           self.rchild.preorder()

tree=BST(None)
l=[50,100,40,80,30,60,20,40,90,70,30,40,90]
for i in l:
    tree.insert(i)

tree.preorder()
print("end")
tree.Delete(60)
tree.preorder()
