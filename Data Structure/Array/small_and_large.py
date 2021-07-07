array=[5,6,8,55,789,2255,485,854,6258,45255,225,2552,8765445678,475862,886,55854,2225,5222,5222,55202,2256,1862,31,4,1521,5,2,15,21,5]
# array.sort(reverse=True)
# for i in array:
#     if str(i)==str(i)[::-1]:
#         print(f"the Longest Palindrone is {i}")
#         break
for i in array:
    for j in array:
        if i==j:
            array.pop(j)
print(len(array))            
