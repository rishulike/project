#J
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==4  and r!=6)or (r==0 and c!=0  and c!=6)or(r==6 and c!=0 and c!=1 and c!=4 and c!=5 and c!=6)or (r==5 and c!=0 and c!=2 and c!=3 and c!=4 and c!=5 and c!=6)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
