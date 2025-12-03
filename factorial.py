num=int(input("enter a number :"))
fact=1
if(num<0):
    print("negative number")
elif(num==0):
    print("have entered zero")
else:
   for i in range(1,num+1):
       fact=fact*i
   print("factorial of thr number is ",fact)
       