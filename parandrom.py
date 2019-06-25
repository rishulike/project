#parndrom
a=(input())
s=""
for l in range(len(a)-1,-1,-1):
    s=s+a[l]
print(s)
if a==s:
    print("string is pallandrom")
else:
    print("string is not pallandrom")
