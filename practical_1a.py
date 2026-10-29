# Practical 1A: Design a Simple Linear Neural Network Model
# Source: SCT Shortest code with original output.docx

print("This is Practical 1A")
x=float(input("Enter the value for x: "))
b=float(input("Enter the value for bias: "))
w=float(input("Enter the value for weight: "))
y=w*x+b
print("Net input = ",y)
print("Apply Activation Function over net input, Ramp Function")
o=0 if y<0 else y if y<=1 else 1
print("output =",o)
