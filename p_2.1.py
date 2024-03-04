print('''
Practical 2 a: Implement AND/NOT function using McCulloch-Pits neuron (use binary data
representation).'''
)

numberOfInput = int(input("Enter Number Of Input "))

# Set The Weight fror inital weight
w1 = 1
w2 = 1 

print("For the ",numberOfInput," input calculate the net input using yin = x1w1 + x2w2")

x1=[]
x2 = []

for j in range(0,numberOfInput):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)

print("x1 = ",x1)
print("x2 = ",x2)

n = x1 * w1
m = x2 * w2

Yin = [ ]


for i in range(0,numberOfInput):
    Yin.append(n[i] + m[i])

print("Yin = ",Yin)

Yin = []

for i in range(0,numberOfInput):
    Yin.append(n[i]-m[i])
print("After assuming one weight as excitatory and the other as inhibitory Yin = ",Yin)

y =[]

for i in range(0,numberOfInput):
    if(Yin[i]>=1):
        ele = 1
        y.append(ele)
    if(Yin[i]<i):
        ele = 0
        y.append(ele)

print("Y = ",y)
