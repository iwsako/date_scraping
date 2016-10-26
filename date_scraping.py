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
            # print temp[4]
            # print(line)
            # bodyの部分だけdataに格納
            if(len(temp) > 4):
                # print(temp[4])
                data.append(temp[4])
    file.close()


# 形態素にかけてリスト化する関数
def make_list():
    # print len(data)
    # 長すぎるため一時省略
    for sentence in data:
        # print sentence
        chasen = tagger.parse(sentence)
        # print(chasen)
        chasen_list = chasen.split("\n")

        for cdata in chasen_list:
            # print cdata
            # 形態素解析した後には先頭に何を形態素解析したのかが一文ついている
            chasen_data.append(re.split(r'\t|,|', cdata))

        # print len(chasen_data)
        # 確認用
        # for textlist in chasen_data:
        #     if len(textlist) > 1:
        #         print("-------")
        #         for text in textlist:
        #             print text
        #         print("-------")


# 日付を抽出
def pick_date():
    for i in range(len(chasen_data)):
        if len(chasen_data[i]) > 2:
            if chasen_data[i][2] == "数":
                # 問題点：円なども名詞、接尾、助数詞のためそれを指定できない
                if chasen_data[i+2][0] == '年間' or chasen_data[i+1][0] == '月間' or chasen_data[i+1][0] == '日間':
                    # おそらく5日間という期間も5日と表示されている
                    print chasen_data[i][0] + chasen_data[i+1][0]
                elif chasen_data[i+1][0] == '年' or chasen_data[i+1][0] == '月' or chasen_data[i+1][0] == '日':
                    print chasen_data[i][0] + chasen_data[i+1][0]


# csvに書き込みをする関数
# def write_csv():
#     with open("")


open_csv()
make_list()
pick_date()
