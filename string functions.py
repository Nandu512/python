p='''Python is an interpreted, high-level and general-purpose programming language.
It is an object-oriented language too, which simply means it can model entities in the real world.

It has a simple, clean syntax, object encapsulation, good library support, and optional named parameters.'''
print('length of string is',len(p))
first=p[0]
print('first charector of paragraph is',first)
last=p[-1]
print('last charector of paragraph is',last)
print('sliced part of string is',p[0:51])
print(p.replace('Python','PYTHON'))
print(p.lower())
print(p.strip())
print(p.split())
i="course"in p
print(i)
k=f"The course description is {len(p)} characters long and has {len(p.split())} words." 
print(k);