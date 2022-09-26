import os
import time
clear = lambda: os.system('cls')
goods = [ 'Apples', 'Pears', 'Bananas', 'Cherries', 'Ananas']
prices = [ 5, 4, 6, 20, 15 ]
count = []
total = 0
delevery = 32.5
for i in range(len(goods)): #vedligeholdelses rettelse
    print(f'{goods[i]} is {prices[i]} kr.')
    print(f'How many {goods[i]} do you want : ')
    count.append(int(input())) #Fejl med append
    price = count[i] * prices[i] #1 fejl her
    print(f'Cost: {price} kr.')
    time.sleep(1)
    clear()
    total = total + price
    print(f'Total : {total} kr.')
if total > 0:
    clear()
    print(f'Delivery charge is {delevery} kr.')
    total = total + price
    print(f'Total : {total} kr.')
    