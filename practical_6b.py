# Practical 6B: Adaptive Resonance Theory (ART)
# Source: SCT Shortest code with original output.docx

import numpy as np
print("This is Practical 6B")
print("Adaptive Resonance Theory Network 1")
L=2; m=3; n=4; rho=.4
te=L/(L-1+n)/2
b=np.full((n,m),te)
t=np.ones((m,n))
s=np.array([[1,1,0,0],[1,0,0,0],[0,0,1,1]])
e=0; yin=np.zeros(3)
while e<3:
 ns=np.sum(s[e]); x=s[e].copy()
 for i in range(3):
  yin[i]=sum(x[j]*b[j,i] for j in range(3))
 J=np.argmax(yin)
 print("J = ",J+1)
 x1=x*t[J]; nx=np.sum(x1); match=nx/ns
 if match<rho:
  yin[J]=-1
  J=np.argmax(yin)
 for i in range(3):
  temp=L-1+nx
  b[i,J]=L*x1[i]/temp
  t[J,i]=x1[i]
 print("b = ")
 print(np.round(b,2))
 print("t = ")
 print(t)
 e+=1
Practical No. 7
