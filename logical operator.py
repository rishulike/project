# logical operator
a=input()
if a=="and":
    print(" no. which are less than 10")
    for a in range(50):
        if a>0 and a<10:
            print(a)
if a=="or":
    print("no. which are greator than 10")
    for a in range(50):
        if a<=10 or a<=30:
            print(a)
if a=="not":
    print("no. which are greator than 20")
    for a in range(50):
        if not a<20:
            print(a)

    

