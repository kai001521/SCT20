# Practical 2A: Generate AND/NOT Function Using McCulloch-Pitts Neural Net
# Source: SCT Shortest code with original output.docx

print("This is Practical 2A")
n=int(input("Enter the number of input "))
print("For the",n,"input calculate the not input")
x1=[]; x2=[]
for i in range(n):
 x1.append(int(input("x1=")))
 x2.append(int(input("x2=")))
print("x1=",x1)
print("x2=",x2)
Yin=[x1[i]+x2[i] for i in range(n)]
print("\nExcitatory weight")
print("Yin=",Yin)
Yin=[x1[i]-x2[i] for i in range(n)]
print("\nInhibitory weight")
print("Yin=",Yin)
print("\n After assuming one weight excitatory and one as inhibitory")
print("Yin=",Yin)
Y=[1 if i>=1 else 0 for i in Yin]
print("Y=",Y)
