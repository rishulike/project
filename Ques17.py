# Z
st=""
for r in range(7):
    for c in range(1,7):
        if((r==0 or r==6)or(r==1 and c==5)or(r==2 and c==4)or(r==3 and c==3)or
           (r==4 and c==2)or(r==5 and c==1)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)


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

#F
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or (r==0)or(r==3 and c!=6 and c!=5)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)
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


#I
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==3)or (r==0 and c!=0  and c!=6)or(r==6 and c!=0 and c!=6)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

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

#L
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or (r==0 and c!=2 and c!=3 and c!=4 and c!=5  and c!=6)or(r==6 and c!=0 and c!=6)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#M
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or(c==6)or (r==1 and c!=2 and c!=3 and c!=4)
            or (r==2 and c!=1 and c!=3 and c!=5 )or(r==3 and c!=1 and c!=2 and c!=4 and c!=5 ) 
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)


#N
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or(c==6)or (r==1 and c!=2 and c!=3 and c!=4 and c!=5)
            or (r==2 and c!=1 and c!=3 and c!=4 and c!=5 )or(r==3 and c!=1 and c!=2 and c!=4 and c!=5 )
            or(r==4 and c!=1 and c!=2 and c!=3 and c!=5 and c!=6)
            or(r==5 and c!=1 and c!=2 and c!=3 and c!=4)
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#O
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0 and r!=0 and r!=1 and r!=5 and r!=6)or(c==2 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5)or(c==1 and r!=0 and r!=2 and r!=3 and r!=4 and r!=6)or
            (c==6 and r!=0 and r!=1 and r!=5 and r!=6) or(c==5 and r!=0 and r!=2 and r!=3 and r!=4 and r!=6)or (c==4 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5)
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#P
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or(r==0 and c!=6)
            or (r==1 and c!=1 and c!=2 and c!=3 and c!=4 and c!=5)or (r==2 and c!=1 and c!=2 and c!=3 and c!=4 and c!=5)or(r==3 and c!=1  and c!=6)   
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#T
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==3)or(r==0)or(r==1 and c!=1 and c!=2 and c!=3 and c!=4 and c!=5)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#Q
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0 and r!=0 and r!=1 and r!=5 and r!=6)or(c==2 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5 )or(c==1 and r!=0 and r!=2 and r!=3 and r!=4 and r!=6)or
            (c==6 and r!=0 and r!=1 and r!=5 ) or(c==5 and r!=0 and r!=2 and r!=3 and r!=4 and r!=6 )or (c==4 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5 and r!=6 )
            or(c==3 and r!=1 and r!=2 and r!=3 and r!=5)
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

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

#V
st=""
for r in range(7):
    for c in range(0,7):
        if (((c==0 and r!=2 and r!=3 and r!=4 and r!=5 and r!=6)or(c==2 and r!=0 and r!=1 and r!=6 and r!=2 and r!=3  )or
             (c==1 and r!=0 and r!=5  and r!=1  and r!=4 and r!=6)or
            (c==6 and r!=2 and r!=3 and r!=4 and r!=5 and r!=6 ) or(c==5 and r!=0 and r!=5 and r!=1 and r!=4 and r!=6 )or (c==4 and r!=0 and r!=1 and r!=2 and r!=3  and r!=6 )or
            (c==3 and r!=0 and r!=4 and r!=1 and r!=2 and r!=3 and r!=5))):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)


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

#Y
st=""
for r in range(7):
    for c in range(0,7):
        if (((c==0 and r!=1 and r!=2 and r!=3 and r!=4 and r!=5 )or(c==2 and r!=0 and r!=1 and r!=6  and r!=5  and r!=3  )or
             (c==1 and r!=0 and r!=2   and r!=3  and r!=4 and r!=6)or
            (c==6 and r!=1  and r!=2 and r!=3 and r!=4 and r!=5 and r!=6  ) or(c==5 and r!=0 and r!=2 and r!=3 and r!=4  and r!=5 and r!=6 )or (c==4 and r!=0  and r!=4  and r!=3 and r!=5 and r!=1   and r!=6 )or
            (c==3 and r!=0 and r!=4 and r!=1 and r!=2 and r!=4 and r!=5 and r!=6))):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#R
st=""
for r in range(7):
    for c in range(0,7):
        if ((c==0)or(r==0 and c!=6)
            or (r==1 and c!=1 and c!=2 and c!=3 and c!=4 and c!=5)or (r==2 and c!=1 and c!=2 and c!=3 and c!=4 and c!=5)or
            (r==3  and c!=6) or (r==1 and c!=0 and c!=1  and c!=4  and c!=5  and c!=2  and c!=6  and c!=3)or (r==4 and c!=2 and c!=3 and c!=4 and c!=5 and c!=6)
            or(r==5 and c!=1 and c!=2 and c!=4 and c!=5 and c!=6)or(r==6 and c!=1 and c!=2 and c!=4 and c!=5 and c!=3)
            ):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#W

st=""
for r in range(7):
    for c in range(0,7):
        if (((c==0)or(c==2 and r!=0 and r!=1 and r!=2 and r!=6  and r!=5  and r!=3  )or
             (c==1 and r!=0 and r!=1 and r!=2   and r!=3  and r!=4 and r!=6)or
            (c==6 ) or(c==5 and r!=0 and r!=1 and r!=2 and r!=3 and r!=4 and r!=6 )or (c==4 and r!=0 and r!=3 and r!=2 and r!=5 and r!=1   and r!=6 )or
            (c==3 and r!=0 and r!=4 and r!=1 and r!=2 and r!=4 and r!=5 and r!=6))):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

#S

st=""
for r in range(7):
    for c in range(0,7):
        
        if ((r==0  and c!=2 and c!=1 and c!=0 )
            or (r==1 and c!=6 and c!=0 and c!=2 and c!=3 and c!=4 and c!=5)or (r==2 and c!=0 and c!=2 and c!=3 and c!=4 and c!=5 and c!=6)or
            (r==3 and c!=5  and c!=1 and c!=0 and c!=6) or (r==4 and c!=0 and c!=1 and c!=2 and c!=4 and c!=6  and c!=3)
            or(r==5  and c!=1 and c!=2 and c!=4 and c!=5 and c!=0 and c!=3)or(r==6 and c!=0  and c!=1  and c!=6 and c!=3)):
            st=st+"*"
        else:
            st=st+" "
    st=st+"\n"
print(st)

