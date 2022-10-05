import re
from typing import final
pattern = (r'^a.*b$',r'^a.+b$',r'^a-*b$',r'^a.[rb]*b$',r'^a.[rb]+b$')
while True:
    for x in pattern:
        while True:
            line = input(f'Input text to match RE {x} : ')
            if re.search(x, line, re.IGNORECASE):
                search = re.search(x, line, re.IGNORECASE)
                print('Bingo !')
                break
            else: 
                print(f"Not correct. Try again for this regex {x}")
    print("You completed all regex")
    break