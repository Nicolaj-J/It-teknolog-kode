f = open(r'8,1\namesfile.txt', 'w')

for i in range(5):
    f.write(input('Write a name: ') + '\n')

f.close()

f = open(r'8,1\namesfile.txt', 'r')

text = f.readlines()
for i in range(5):
    print(text[i].rstrip('\n'))


