names= ['Olaf','Peter','Lars','John']
number = ['123','456','789','146']

for i in range(len(names)):
    print('write', i +1, 'to get', names[i] +"´s",'phonenumber')
x = int(input())
print(number[x-1])