# Pattern Designing
a=int(input(" "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()
for i in range(a,1,-1):
    for j in range(i,1,-1):
        print(" * ",end=" ")
    print()

# Pattern Designing
n=int(input())
for i in range(n,1,-1):
    for j in range(i,1,-1):
        print(" * ",end=" ")
    print()
for i in range (1,n+1):
    for j in range(1,i+1):
        print(" * ",end=" ")
    print()

# Pattern designing
import string
print(list(string.ascii_lowercase))
ls=list(string.ascii_lowercase)
n=(input())
for n in range(len(ls)):
    for m in range(0,n+1):
        print(ls[m],end=" * ")
    print()
        


