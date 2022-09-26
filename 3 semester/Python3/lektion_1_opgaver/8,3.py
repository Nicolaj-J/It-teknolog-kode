import csv, sys
from statistics import mean
path = r'C:\Users\nicol_kw6jk4h\mu_code\Projekter\It-teknolog-kode\3 semester\Python3\data\MPF_subset_data.csv'
temperature = []
avgtemperature = []
i = 0
with open(path, newline="") as f:
    reader = csv.reader(f)
    
    try:
        for i in range(3,6):
            f.seek(0)
            next(reader)
            next(reader)
            for row in reader:
                temperature.append(float(row[i]))
            total = sum(temperature)
            length = len(temperature)
            avgtemperature.append(float(total)/float(length))
            temperature.clear()
    except csv.Error as e:
        pass
avgtemperature.append(sum(avgtemperature)/len(avgtemperature))
print(avgtemperature)