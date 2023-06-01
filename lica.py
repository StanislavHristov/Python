figura=input("Enter figura:")
if figura=="triangle":
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    P=a+b+c
    print ("P = ",P)
    S=a*b
    print ("S = ",S)
elif figura=="square":
    a=int(input("a= "))
    P=a*4
    print ("P = ",P)
    S=a*a
    print ("S = ",S)
elif figura=="rectangle":
    a=int(input("a= "))
    b=int(input("b= "))
    P=a*2+b*2
    print ("P = ",P)
else:
    print("Unknown shape")

