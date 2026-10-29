# Practical 7C: Fuzzy Membership Functions and Fuzzification
# Source: SCT Shortest code with original output.docx

print("This is Practical 7C")
def tri(x,a,b,c):
 return 0.0 if x<=a or x>=c else 1.0 if x==b else (x-a)/(b-a) if x<b else (c-x)/(c-b)
print("Temperature Fuzzification Results")
print("---------------------------------")
for t in [5,18,25,37,45]:
 c=tri(t,0,10,20); co=tri(t,15,25,35); h=tri(t,30,40,50)
 print(f"\nTemperature: {t}°C")
 print(f"Cold : {c:.2f}")
 print(f"Comfortable : {co:.2f}")
 print(f"Hot : {h:.2f}")
Practical No. 8
