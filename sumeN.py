n=int(input("Enter the first N nutural numbers:"))
s=0
for i in range(1, n+1):
    s=s+i
print(f"Sum of the first {n} natural numbers: {s}")