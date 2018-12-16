print('Enter the list of numbers separated by space')
a=list(input().split())
b=[]
for item in a:
        item1=item[::-1]
        c=list(item1)
        for i in range(3,len(c),4):
            c.insert(i,",")
        int1=''.join(c)
        int2=int1[::-1]
        b.append(int2)
print(b)
