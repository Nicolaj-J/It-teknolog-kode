filenames = ['text1','text2','text3']

for i in range(len(filenames)):
    path = f'8,2/{filenames[i]}.txt'
    f = open(path, 'r')
    print(f.readline())
