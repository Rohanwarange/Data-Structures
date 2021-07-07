# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:56:36 2021

@author: ROHAN
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:40:24 2021

@author: ROHAN
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:17:41 2021

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
                    
      # for searching the element is present or not   
           
    # def searchbst(self,data):
    #     if self.key==data:
    #         print("data is present in tere")
    #     else:
    #         if self.key>data:
    #            if self.lchild:
    #                self.lchild.searchbst(data)
    #            else:
    #                print("Node is Not Present in tree")
    #         else:
    #             if self.rchild:
    #                 self.rchild.searchbst(data)
    #             else:
    #                 print("Node is Not Present in tree")
    
    # preorder traversal
    
    # def preorder(self):
    #     if self.lchild:
    #         self.lchild.preorder()
    #     if self.rchild:
    #        self.rchild.preorder()
    
    # def Inorder(self):
    #     if self.lchild:
    #           self.lchild.Inorder()
    #     print(f"{self.key}---> ",end="")
    #     if self.rchild:
    #           self.rchild.Inorder()
              
    def Postorder(self):
        if self.lchild:
              self.lchild.Inorder()
        if self.rchild:
              self.rchild.Inorder()   
        print(f"{self.key}---> ",end="")
                    
                   
            
            
                    
tree=BST(None)  
l=[10,20,30,40,50,100,0,56.85,89,45]                  
for i in l:
    tree.insert(i)
# tree.searchbst(9) 
# tree.preorder() 
tree.Inorder()