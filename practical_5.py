# Practical 5: Hopfield Network Model for Associative Memory
# Source: SCT Shortest code with original output.docx

import numpy as np
def net(j,w,x,t,yin,y):
 t=sum(y[i]*w[i][j] for i in range(4))
 yin[j]=x[0][j]+t
 y[j]=1 if yin[j]>0 else y[j] if yin[j]==0 else -1
 return yin,y
print("This is Practical 5")
print("Discrete Hopfield network")
theta=0
x=np.array([1,1,1,-1])
w=np.outer(x,x)
print("\nWeight matrix with self-connection:")
print(w)
np.fill_diagonal(w,0)
print("\nWeight matrix with no self-connection:")
print(w)
x1=np.array([[1,1,1,-1]])
y=[1,1,1,-1]; yin=[0]*4
print("\nBy Asynchronous updation method")
print("\nThe net input calculated is : ")
for j in [1,3,2,0]: yin,y=net(j,w,x1,0,yin,y)
print("\nThe output calculated from net input is :")
print(y)
Practical No. 6
