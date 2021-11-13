# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<40:
#         count=count+1
#     i+=1 
# print(count)

# place=['Delhi','Gujrat','Rajesthan','Punjab','Kerla']
# i=len(place)-1
# b=[]
# while i+1:
#     print(place[i])
#     i=i-1



# i=int(input("Enter the number: "))
# a=0
# b=0
# while i>0:
#     c=i//10
#     d=i%10
#     a=a + d*2**b
#     b +=1
#     i=c
# print("Decimal number is",a)      


a=[0,1,1,1,1,0,1,1]
i=0
sum=0
sum1=0
number=6
while i<len(a):
    b=a[number]
    sum=(2**i*b)
    number-=1
    i+=1
    sum1+=sum
print(sum1)    


