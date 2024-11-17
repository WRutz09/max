lar=0
print("Enter the number:")
for i in range(1,11):
    n=int(input())
    if i==1:
        lar=n
    elif n>lar:
        lar=n
print("Largest number is:",lar)
    
