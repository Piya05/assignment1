L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
L3=[]
for i in range(len(L1)):
  if i%2==0:
    L3.append(L1[i])
for i in range(len(L2)):
  if i%2!=0:
    L3.append(L2[i])

print(f"L3={L3}")
