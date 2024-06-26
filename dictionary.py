dict = {'a':1, 'b':2, 'c':3, 'd':4}
print(dict)

del dict['b']
print(dict)

dict['a'] = 10
print(dict)

if 'c' in dict:
 print(True)
else:
 print(False)

print(list(dict.keys()))
 

