# try:
#     num=int(input("enter numo"))
#     deno=int(input("enter deno"))

#     print(int(num/deno))

# except:
#     print("Error : Deno cannot be zero")
#     print()

try:    
    num=int(input("enter no to reciprocal it : "))
    if num%2==0:
         print(1/num)
    

except:
    print("Error : Deno cannot be zero")
    
else:
    print("Error : enter even no.")