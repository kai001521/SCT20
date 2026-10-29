# Practical 3B: Write a Program to Implement Delta Rule
# Source: SCT Shortest code with original output.docx

import numpy as np
print("This is Practical 3B")
np.set_printoptions(precision=20)
x=np.array([float(input("Initial inputs:")) for i in range(3)])
w=np.array([float(input("Initial weights:")) for i in range(3)])
d=np.array([float(input("Desired output:")) for i in range(3)])
a=float(input("Enter learning rate :"))
y=x*w
print("actual",y)
print("desired",d)
while not np.array_equal(d,y):
 w+=a*(d-y)
 y=x*w
 print("weights",w)
 print("actual",y)
 print("desired",d)
print("Final output")
print("corrected weights",w)
print("actual",y)
print("desired",d)
