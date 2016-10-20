# coding:utf-8

import sys
import csv
import MeCab
import re

csv = sys.argv
tagger = MeCab.Tagger()
data = []
chasen_buffer = []
chasen_list = []
chasen_data = []


def change_morpheme(data):
    chasen = tagger.parse(data[4])
    chasen_list = chasen.split("\n")
    # print(chasen_list[0])

    for cdata in chasen_list:
            chasen_data.append(re.split(r'\t|,|', cdata))
            #print(chasen_data[0])

    print(chasen_data[0][2])


def open_csv():
    with open("Great_East_Japan_Earthquake.csv", "rb") as file:
        for line in file:
            data.append(line)


open_csv()
change_morpheme(data)
