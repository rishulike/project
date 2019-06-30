#K
st=""
for r in range(7):
    for c in range(7):
        if((c==3)or(r==0 and c==6)or(r==1 and c==5)or(r==2 and c==4)
           or (r==3 and c==3 and r==4)or(r==4 and c==4)or(r==5 and c==5)
           or(r==6 and c==6)):
            st=st+"* "
        else:
            st=st+"  "
    st=st+"\n"
print(st)
