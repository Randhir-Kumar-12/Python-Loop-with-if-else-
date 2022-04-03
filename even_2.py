# The first 10 even natural numbers
a=int(input("Enter the fist N even natural numbers: "))
b=a*2+1
for i in range(1, b):
    if i%2==0:
        print(i, end=' ')

print()

# Odd numbers in reverse order
c=int(input("Enter the fist N even natural numbers: "))
n=c*2
while n>=1:
    if n%2==0:
        print(n, end=' ')
    n=n-1   