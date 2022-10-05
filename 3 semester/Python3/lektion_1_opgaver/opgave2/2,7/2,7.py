from optparse import Values


agehash = {'Peter' : 34, 'Peter' : 29,'Lars' : 41,}

for key, value in agehash.items():
    print(f'{key} is {value} years old.')
    print( '-' * 50 )
agehash['Peter'] = 35 
agehash['Andrew'] = 44
for key in agehash.keys():
    print(f'{key} is {agehash[ key ]} years old')

print('Sum age: ', sum(agehash.values()))
        