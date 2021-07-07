import collections 
from collections import Counter
array=[5,6,8,5,2,15,21,5]
C=Counter(array)
print(C[5])

# d={}
# d=collections.OrderDict()
# # print(array[::-1])
# a=0
# for i in array:
#     for j in range(len(array)):
#         if i==array[j]:
#            a+=1
#     d[i]=a
#     a=0
# for i,k in d.items():
#     print(i,k)           


# total=0
# for i in array:
#     total+=i
#     print(total)
# print(total)