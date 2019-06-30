#E
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or (r==0)or(r==3)or (r==6)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
