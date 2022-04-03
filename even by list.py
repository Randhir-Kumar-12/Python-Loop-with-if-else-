list1=[]
print(f"list1={list1}")
b=int(input("Enter the first N even natural numbers:"))
n=b*2+1
for i in range(1,n):
    if i%2==0:
        list1.append(i)

for item in list1:
    print(item, end=' ')
print()
print(f"list1={list1}")


# Even numbers--->in revers order
list2=[]
print(f"list2={list2}")
g=int(input("Enter the first N even natural numbers:"))
h=g*2+1
for i in range(1,h):
    if i%2==0:
        list2.append(i)

x=g-1
while x>=0:
    print(list2[x], end=' ')
    x=x-1
print()

print(f"list2={list2}")

