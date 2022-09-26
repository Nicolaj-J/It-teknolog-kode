import random
jokenr = 0

jokelist = ["joke1", "joke2", "joke3", "joke4"]
print(jokelist)
for x in range (3):
    jokelist.append("orange")
print(jokelist)
jokenr = random.randrange(len(jokelist))
print(jokenr)
print(jokelist[jokenr])
