import csv
path = r"C:\Users\nicol_kw6jk4h\mu_code\Projekter\It-teknolog-kode\3 semester\Python3\data\syslog"
f = open(path)
file = csv.reader(f)
viagra = 0
spam = 0
for row in file:
    line = str(row)
    if line.find("viagra.com") != -1:
        viagra += 1
    elif line.find("spam.com") != -1:
        spam += 1


print("Viagra: ", viagra)
print("Spam: ", spam)
