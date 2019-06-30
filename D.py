#D
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==2)or (r==0 and c!=6)or (c==6 and r!=0 and r!=6)or (r==6 and c!=6)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
