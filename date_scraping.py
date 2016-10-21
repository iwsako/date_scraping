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


def open_csv():
    with open("Great_East_Japan_Earthquake.csv", "rb") as file:
        for line in file:
            temp = line.split(",")
            # bodyの部分だけdataに格納
            if(len(temp) > 4):
                data.append(temp[4])


def make_list():
    # print len(data)
    # 長すぎるため一時省略
    for sentence in data[:7]:
        chasen = tagger.parse(sentence)
        # print(chasen)
        chasen_list = chasen.split("\n")

        for cdata in chasen_list:
                chasen_data.append(re.split(r'\t|,|', cdata))

        print len(chasen_data)
        # 確認用
        for textlist in chasen_data:
            if len(textlist) > 1:
                print("-------")
                for text in textlist:
                    print text
                print("-------")


# 日付を抽出
def pick_date():
    num_buffer = ""
    for textlist in chasen_data:
        if len(textlist) > 2:
            # print(textlist[2])
            # 問題点：円なども名詞、接尾、助数詞のためこのやり方では日にち抽出できない
            if textlist[1] == "名詞" and textlist[2] == "接尾" and textlist[3] == "助数詞":
                print(num_buffer + textlist[0])
                # print(textlist[0])

            # 問題点：億などの語句も数という形態素をもっている
            if str(textlist[2]) == "数":
                num_buffer = textlist[0]


open_csv()
make_list()
pick_date()
