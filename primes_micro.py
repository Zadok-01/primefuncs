m=20;p=[2]
for c in range(3,m+1,2):
 f=True
 for d in p:
  if d*d>c:break
  if c%d==0:f=False;break
 if f:p.append(c)
print(p)