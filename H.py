#H
st=""
for r in range(7):
    for c in range(1,7):
        if ((c==1 or c==6 or r==3)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
