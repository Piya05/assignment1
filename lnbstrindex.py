str1=[]
evenstrlist=[]
oddstrlist=[]
str1=input("Enter the string :")
strlen=len(str1)
for i in range(strlen):
  if i%2==0:
    evenstr=str1[i]
    evenstrlist.append(evenstr)
  else:
    oddstr=str1[i]
    oddstrlist.append(oddstr)
if strlen>7:
  print(f"The output string is :{evenstrlist}")
else:
  print(f"The output string is :{oddstrlist}")

