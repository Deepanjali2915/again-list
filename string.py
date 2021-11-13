# name=[20,"deepu","anki",4,8,"223"]
# # o/p=["deepu","anki","223"]
# i=0
# a=[]
# while i<len(name):
#     if type(name[i])==str:
#         a.append(name[i])
#     i+=1
# print(a)

# a=[20,"Deepu",32,34,32,44.2]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])  
#     i+=1
# print(b)          
# o/p=[1,2,3,4,5,6,7,8,9]
# num=[1,2,[3,4,5,[6,7],8,9]]
# i=0
# a=[]
# sum=0
# while i<len(num):
#     if type(num[i])==list:
#         j=0
#         while j<len(num[i]):
#             if type(num[i][j])==list:
#                 k=0
#                 while k<len(num[i][j]):
#                     a.append(num[i][j][k])
#                     sum=sum+num[i][j][k]
#                     k+=1  
#             else:
#                 a.append(num[i][j])
#                 sum=sum+num[i][j]
#             j+=1     
#     else:
#         a.append(num[i])
#         sum=sum+num[i]        
#     i+=1  
# print(a)      
# print(sum)



# a=[6,7,8,1,3,5,9,12]
# i=1
# b=[]
# while i<len(a):
#     if i%2!=0:
#         b.append(a)
#         print(a[i],end=" ")
#     i+=1

# a=["Amisha","Manjeet","Deepanjali","Nandini"] 

# i=0
# count=0
# b=[]
# while i<len(a):
#     b.append(len(a[i]))
#     i+=1
# print(b)
# print(a[i])




