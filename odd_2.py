a=int(input("Enter the first N odd natural numbers: "))
b=a*2+1
for i in range(1,b):
    if i%2!=0:
        print(i, end=' ')

print() # for new line

# Odd numbers in reverse
d=int(input("Enter the first N odd natural numbers: "))
n=d*2
while n>=1:
    if n%2!=0:
        print(n, end=' ')
    n=n-1    
