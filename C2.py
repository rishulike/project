#C
st=""
for r in range(7):
    for c in range(7):
        if ((c==0 and (r!=0 and r!=6))
            or (r==0 or r==6)and(c>0 and c<5)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
