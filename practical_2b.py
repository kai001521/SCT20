# Practical 2B: Generate XOR Function as a Non-Linearly Separable Problem Using a Suitable Multilayer Neural Network
# Source: SCT Shortest code with original output.docx

import numpy as np
print("This is Practical 2B")
print("Enter weights")
w11=int(input("weight w11=")); w12=int(input("weight w12="))
w21=int(input("weight w21=")); w22=int(input("weight w22="))
v1=int(input("weight v1=")); v2=int(input("weight v2="))
print("Enter threshold value")
t=int(input("theta="))
x1=np.array([0,0,1,1]); x2=np.array([0,1,0,1])
z=np.array([0,1,1,0])
z1=x1*w11+x2*w21; z2=x1*w12+x2*w22
print("z1",z1); print("z2",z2)
y1=(z1>=t).astype(int); y2=(z2>=t).astype(int)
yin=y1+v1+y2+v2
y=(yin>=t).astype(int)
print("yin",yin)
print("Output of Net")
print("y=",y)
print("z=",z)
Practical No. 3
