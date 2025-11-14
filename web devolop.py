web=["raju","sreehari","binu"]
data=["balan","arjun","kohili"]
uiux=["deepika","abhinesh","meenu"]
all_participants=web+data+uiux
print('all partcipants are',all_participants)
web.append("abhi")
print('updated web development',web)
data.insert(1,"kevin")
print('updated data science',data)
uiux.pop()
print('updated uiux is',uiux)
new_data=data.copy()
data.clear()
print('copied data is',new_data)
print('first two web devolopment participants',web[0:2])
print('check asha in list','asha'in all_participants )
name_lengths = [len(name) for name in new_data]
print("Name lengths (Data Science):", name_lengths)
first_participants=(web[0],new_data[0],uiux[0])
print('tuple of first participants is',first_participants)








