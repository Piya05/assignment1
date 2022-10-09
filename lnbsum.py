intlist=[]
sum=0
for i in range(5):
  number=int(input(f"Enter the integer {i+1} :"))
  if number >=9:
    sum+=number
    intlist.append(number)
print(f"The sum of {intlist} is :{sum}")
