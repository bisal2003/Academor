# def add(num1,num2):
#     sum=num1+num2
#     print(sum)

# num1=int(input("enter"))

# add(10,num1)
# add(2,6)

# calculator

def calc(a,b,c):

    if c==1:
        return a+b
    elif c==2:
        return a*b
    elif c==3:
        return a-b
    elif c==4:
        return a/b
    else:
        print("invalid input")
        return calc(a,b,c)
    

def choice():
    while True:
        print('''Enter 1 for add, 2 for multiply, 
3 for subtract, 4 for divide''')
        c = int(input("Enter your choice: "))
        if c in [1, 2, 3, 4]:
            return c
        else:
            print("Invalid choice. Please try again.")


a=int(input("Enter 1st no"))
b=int(input("Enter 2nd no"))

c=choice()


print(calc(a,b,c))




