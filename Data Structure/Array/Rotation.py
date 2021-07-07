# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:33:48 2021

@author: ROHAN
"""
# l1=[10,20,30,40,50,60,70,80]
# def RightRotate(l1,k):
#     k=k%len(l1)
#     for i in range(k):
#         e=l1.pop()
#         l1.insert(0,e)
#     return l1
# print(RightRotate(l1,4))

l1=[10,20,30,40,50,60,70,80]

def leftRotate(l1,k):
    k=k%len(l1)
    for i in range(k):
        e=l1.pop()
        l1.insert(i,e)
    return l1
print(leftRotate(l1,4))#


        
