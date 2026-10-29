# Practical 4: Backpropagation Neural Network
# Source: SCT Shortest code with original output.docx

import numpy as np, math
print("This is Practical 4")
np.set_printoptions(precision=4)
v1=np.array([.6,-.3]); v2=np.array([-.1,.4])
w=np.array([-.2,.4,.1]); b=np.array([.3,.5])
x=np.array([.1,.2]); a=.25
print("calculate net input to z layer")
zin=[round(b[i]+x[0]*v1[i]+x[1]*v2[i],4) for i in range(2)]
print("zin=",zin)
print("Apply activation function to calculate output")
z=[round(1/(1+math.exp(-i)),4) for i in zin]
print("z=",z)
print("calculate net input to output layer")
yin=w[0]+z[0]*w[1]+z[1]*w[2]
print("yin=",yin)
print("calculate net output")
y=round(1/(1+math.exp(-yin)),4)
print("y=",y)
dk=round((1-y)*y*(1-y),4)
print("dk",dk)
dw=[a*dk*z[0],a*dk*z[1],a*dk]
print("compute error portion in delta")
din=[dk*w[i] for i in (1,2)]
print("din=",din)
print("error in delta")
fzin=[round(i*(1-i),4) for i in z]
d=[round(din[i]*fzin[i],4) for i in range(2)]
print("fzin=",fzin)
print("d=",d)
dv=[[a*d[j]*(x[i] if i<2 else 1) for j in range(2)] for i in range(3)]
print("Changes in weight\nbetween input and hidden layer")
print(dv)
print("Final weights of network")
v1+=dv[0]; print("v1=",v1)
v2+=dv[1]; print("v2=",v2)
b+=dv[2]; print("b=",b)
w+=np.array([dw[2],dw[0],dw[1]])
print("w=",w)
