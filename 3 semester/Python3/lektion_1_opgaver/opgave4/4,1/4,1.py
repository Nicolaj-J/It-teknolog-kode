list = []

for i in range(0,10):
    list.append(int(input(f"Write number {i+1}: ")))
print("Sum",sum(list))
print("Average", sum(list)/len(list))
print("Lowest number", min(list))
print("Highest number",max(list))