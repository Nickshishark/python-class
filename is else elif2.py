scored1=int(input("what is your first scored? "))
scored2=int(input("What is your second scored? "))
if (scored1+scored2)/2<50:
    print("you failed, try again next year. ")
elif (scored1+scored2)/2<80:
    print("you got a good, good job.")
else:
    print("you got a very good, good job.")