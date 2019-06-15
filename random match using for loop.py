print("Welcome to My world")
a=str(input())
print("welcome to visual form",a)
print("here you have 3 chance to  exit from my world")
print("you have need enter 3 values if your values matched within random value than you got exit otherwise you never got exit")
print("kyunki baby Ram nhi Ravan hoo mai")
import random as ran
b=ran. randint(0,100)
for i in range(0,3):
    i=int(input())
if i<b:
    print("number is small")
elif i>b:
    print("number is greator")
else:
    print("number is matched")
print(b)

