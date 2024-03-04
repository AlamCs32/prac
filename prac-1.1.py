print("Practical 1 a: Design a simple linear neural network model.")

x = float(input("Enter Value Of X: "))
w = float(input("Enter Value Of W: "))
b = float(input("Enter Value Bias b: "))

net = int(w*x+b)

if(net>0):
    out = 0
elif(net>=0) & (net <=1):
    out = net
else:
    out = 1

print("net= ",net)
print("output= ",out)