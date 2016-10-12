# coding: utf-8

import csv

data = []

with open("Great_East_Japan_Earthquake.csv", "rb") as f:
    reader = csv.reader(f)

    for row in reader:
        data.append(row)

# リストの状態では数字の羅列になるためn次元のリストだとその階層まで下げる必要がある
for t in data:
    # for s in t[3]:
        print(t[4])
