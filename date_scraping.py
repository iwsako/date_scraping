# coding: utf-8

import csv

data = []

with open("Great_East_Japan_Earthquake.csv", "rb") as f:
    reader = csv.reader(f)

    for row in reader:
        data.append(row)

print(data)
