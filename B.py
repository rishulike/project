#B
st=""
for r in range(7):
    for c in range(1,7):
        if ((c==1)or ((r==0 or r==3 or r==6)and(c>1 and c<4))or(c==4 and (r!=0 and r!=3 and r!=6 ))) :
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
