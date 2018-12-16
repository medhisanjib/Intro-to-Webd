print("Enter the list of names separated by a comma(,): ")
a=list(input().split(','))
print("The list of entered names is: ")
print(a)
print("The abbreviations for the given names are: ")

b=[]
for item in a:
    c=[]
    list(item)
    c.append(item[0])
    d=len(item)
    for i in range(d):
        if item[i]==' ':
            c.append(item[i+1])

    str1=''.join(c)
    b.append(str1)

print(b)
