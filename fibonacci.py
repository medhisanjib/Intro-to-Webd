print("Enter number of terms upto which series is to be calculated")
n=int(input())
print('0',end='\n')
print('1',end='\n')
first=0
second=1
for num in range(n-2):
        third=first+second
        print(third)
        first=second
        second=third
