# Practical 7A: Implement Membership Operators in and not in Python
# Source: SCT Shortest code with original output.docx

print("This is Practical 7A")
print("Membership and Identity Operators | in, not in")
def overlapping(a,b):
 for i in a:
  if i in b: return 1
 return 0
l1=[2,3,4,5]; l2=[6,6,8,6]
print("Overlapping" if overlapping(l1,l2) else "Not Overlapping")
