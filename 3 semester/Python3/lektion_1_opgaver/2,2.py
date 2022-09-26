goods = {'Apples' : 5, 'Peas' : 4, 'Bananas' : 6, 'Pineapples' : 20}
total = 0
for key, value in goods.items():
    total += (int(input(f'How many {key} of {value}kr \n')) * int(value))
total = total + 32.50
print(f'To be payed in full: {total} kr.')