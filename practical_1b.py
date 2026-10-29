# Practical 1B: Calculate the Output of Neural Net Using Both Binary and Bipolar Sigmoidal Function
# Source: SCT Shortest code with original output.docx

import math
print("This is Practical 1B")
n=int(input("Enter no. of input neurons: "))
print("Enter input")
x=[float(input()) for i in range(n)]
print(x)
print("Enter weight")
w=[float(input()) for i in range(n)]
print(w)
print("The net input can be calculated as Yin=x1w1+x2w2+x3w3")
ynet=round(sum(x[i]*w[i] for i in range(n)),3)
print("Net input for y neuron=",ynet)
print("Apply activation function over net input A) Binary Sigmoidal activation function")
print(round(1/(1+math.exp(-ynet)),3))
print("Apply activation function over net input B) Bipolar Sigmoidal activation function")
print(round(2/(1+math.exp(-ynet))-1,3))
Practical No. 2
