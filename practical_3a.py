# Practical 3A: Write a Program to Implement Hebb’s Rule
# Source: SCT Shortest code with original output.docx

print("This is Practical 3A")
X=[[1,1],[1,-1],[-1,1],[-1,-1]]
print("input=")
for x in X: print(x)
Y=[1,-1,-1,-1]
print("Target=",Y)
w=[0,0]
print("Intial weight values=",w)
for i in range(len(X)):
 for j in range(len(w)): w[j]+=X[i][j]*Y[i]
 print(i,"Iteration, weights value=",w)
