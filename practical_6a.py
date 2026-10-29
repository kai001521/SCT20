# Practical 6A: Kohonen Self-Organizing Feature Map
# Source: SCT Shortest code with original output.docx

import numpy as np
print("This is Practical 6A")
print("Kohonen self-organizing feature map")
x=np.array([[0,0,1,1],[1,0,0,0],[0,1,1,0],[0,0,1,1]])
a=0.5
print("The weight matrix is : ")
w=np.array([[.2,.9],[.4,.7],[.6,.5],[.8,.3]])
print(w)
print("The Learning rate of this epoch is: ",a)
k=0
while k<4:
 D=np.sum((w-x[k,:,None])**2,axis=0)
 J=0 if D[0]<D[1] else 1
 print(f"\nInput Pattern {k+1}: {x[k]}")
 print(f"The winning unit is: {J+1}")
 print("Weight updation: ")
 w[:,J]+=a*(x[k]-w[:,J])
 print("Updates weight matrix: ")
 print(w)
 k+=1
