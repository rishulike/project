#U
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0 and r!=6)or(c==6 and r!=6)or (r==6 and c!=0 and r!=1 and r!=5 and c!=6)) :
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

