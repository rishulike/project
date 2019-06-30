#G
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0 and r!=0 and r!=6)or (r==0 and c!=0 and c!=1 and c!=4 and c!=5 and c!=6)or(c==2 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5)   
            or(r==3 and c!=1 and c!=2 and c!=6)or(r==6 and c!=0 and c!=3 and c!=4 and c!=5 and c!=6)or
            (r==5 and c!=1 and c!=2 and c!=3 and c!=5 and c!=6)or (c==4 and r!=0 and r!=1 and r!=2 and r!=5 and r!=6 )):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
