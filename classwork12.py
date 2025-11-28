#You are helping to create a simple name game for a birthday event.
#Ask the user to enter a list of names of invited guests (comma-separated).
#Remove any duplicate names.
#Randomly choose one name from the final list to play a game.
#Reverse the selected name and display it.
#Also, print the total number of unique names and round the square root of that number to the nearest whole number.
import random
import math
from collections import OrderedDict
orginal=['arun','amit','rahul','keshav','amit','rahul']
print("orginal list is:"+str(orginal))
result=list(OrderedDict.fromkeys(orginal))
print("list after removing duplicates:"+str(result))
k=random.choice(result)
print("selecting random name:",k)
reverse_name=k[::-1]
print("reversed name is: ",reverse_name)
count_name=len(result)
print("total no of unique names:",count_name)
rounded_sqrt=round(math.sqrt(count_name))
print("rounded square root is:",rounded_sqrt)


