#Your tasks are:
#Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
#Count how many days the class was full.
#Calculate and print the total attendance for all 5 days.
attendance = [18, 20, 19, 15, 21]
for x in attendance:
    if x>=20:
        print("full")
    else:
        print('not full')   

total_attendance = 0
for x in attendance:
    total_attendance += x
print("Total attendance:", total_attendance)
total_days=0
for x in attendance:
    if x>=20:
     total_days += 1
print('counting how many days the class was full:',total_days)
        