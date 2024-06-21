with open('data.txt','r') as f:
    data=f.read()
    


f.close()
print(data)

f = open("data.txt",'w')
f.write("how are u")
f.close()

with open('data.txt','r') as f:
    data=f.read()
    


f.close()

# data1=f.read()

print(data)
