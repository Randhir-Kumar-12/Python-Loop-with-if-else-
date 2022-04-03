# The first 10 even natural numbers
for i in range(1,21):
    if i%2==0:
        print(i, end=' ')

print()

# Odd numbers in reverse order
n=20
while n>=1:
    if n%2==0:
        print(n, end=' ')
    n=n-1    