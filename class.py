#You are helping a small stationery shop owner manage a simple list of items.
#First, ask the user to enter the name of a new item.
#If the file items.txt does not exist, create it and write the item into it.
#If the file exists, open it in append mode and add the new item.
#After writing, display the full list of items from the file to the user

import os
item = input("Enter the name of a new item: ")
filename = "item.txt"
if os.path.exists(filename):
    with open(filename, "a") as file:
        file.write(item + "\n")
else:
    with open(filename, "w") as file:
        file.write(item + "\n")
print("\nFull list of items:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
