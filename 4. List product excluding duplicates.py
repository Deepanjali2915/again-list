list=[1,3,5,6,3,5,6,1]
i=0
a=[]
b=1
while i<len(list):
    j=list[i]
    if j not in a:
        a.append(j)
        b=b*a[i]
    i+=1
print(b)    