# num=int(input("Enter the number: "))
# i=0
# a=[]
# b=[]
# for i in range(num):
#     value=int(input("Enter the number: "))
#     a.append(value)

a=[9,5,4,7]
i=0
while i<len(a)-1:
   if a[i]>a[i+1]:
      c=a[i]
      a[i]=a[i+1]
      a[i+1]=c
      # b.append(c)
   i+=1
print(a)
# print(b)

# while i<len(a):
#     j=0
#     max=0
#     while j<len(a):
#         type(a)==list
#         if a>max:
#             max=a
#         i+=1
# print(max) 


# mylist = []
# b=[]
# size = int(input('How many elements you want to enter? '))
# print('Enter', str(size), 'positive numbers')
# for i in range(size):
#    data = int(input())
# mylist.append(data)
# max = 0
# for data in mylist:
#    if data > max:
#     max = data
#     b.append(max)
# print('The largest number in list is', max,"\n",b)

