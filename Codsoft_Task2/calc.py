def add(a,b):
    print(a,"+",b,"=",a+b)
def sub(a,b):
   print(a,"-",b,"=",a-b)
def div(a,b):
    if b==0:
        print("Divide by zero error, please try again")
    else:
        print(a,"/",b,"=",a/b)
def mul(a,b):
    print(a,"*",b,"=",a*b)
ans='Y'
while (ans=='Y' or ans=='y'):
    a=int(input("Enter first number : "))
    b=int(input("Enter the second number : "))
    print()
    print("Choose an operation to be performed : ")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    ch=input("Enter your choice : ")
    print()
    if ch=='1':
        add(a,b)
    elif ch=='2':
        sub(a,b)
    elif ch=='3':
        mul(a,b)
    elif ch=='4':
        div(a,b)
    else:
        print("Invalid choice, please try again")
    ans=input("Do you want to continue? Y/N  : ")

