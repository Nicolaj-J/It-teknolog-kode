import re
import os
import csv
path = r'C:\Users\nicol_kw6jk4h\mu_code\Projekter\It-teknolog-kode\3 semester\Python3\data\MPF_subset_data.csv'
spams = {r"viagra.com": 0, r"spam.com": 0}
with open(path, "r") as f:
    for line in f:
        for spam, count in spams.items():
            if re.search(spam + '.*ACCEPT', line, re.I):
                spams[spam] = count + 1
for spam, count in spams.items():
    print("Source: %s Count:%d" % (spam, count))
