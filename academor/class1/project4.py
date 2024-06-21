# list=[1,2,3,4]

# for i in range(2):
#     for j in range(2):
#         # print(f"i={i}, j= {j}")
#         print(f"{i} , {j}")

for i in range(5):
    for j in range(5,i,-1):
        print(" ", end = "")
    for k in range (i+1):
        print("* ", end="")
    print()

for i in range(5):
    for j in range(5,5-i,-1):
        print(" ", end = "")
    for k in range (5-i):
        print(" *", end="")
    print()



