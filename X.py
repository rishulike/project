#X
st=""
for r in range(7):
    for c in range(0,7):
        if (((c==0 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5 )or(c==2 and r!=0 and r!=1 and r!=6  and r!=5  and r!=3  )or
             (c==1 and r!=0 and r!=2   and r!=3  and r!=4 and r!=6)or
            (c==6 and r!=1  and r!=2 and r!=3 and r!=4 and r!=5  ) or(c==5 and r!=0 and r!=2 and r!=3 and r!=4 and r!=6 )or (c==4 and r!=0 and r!=3 and r!=5 and r!=1   and r!=6 )or
            (c==3 and r!=0 and r!=4 and r!=1 and r!=2 and r!=4 and r!=5 and r!=6))):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

