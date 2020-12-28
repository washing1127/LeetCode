# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/28 18:15
# File: change_readme.py
# Desc:
import os
import glob

with open('README.md', 'r', encoding='utf-8')as r:
    readme_data = r.read().strip().split('|:---:|:---:|---|\n')[1].split("\n")

folders = [i for i in glob.glob("*") if os.path.isdir(i)]

print(folders)

done_dic = {}
for i in readme_data:
    num = i[-9:-5]
    done_dic[num] = i

for num in folders:
    if num not in done_dic.keys():
        name = input(f"编号是多少?直接回车为{num}") or num
        color = input(f"color应该是？直接回车为 green") or 'green'
        with open(name + '/' + name + '.txt', 'r', encoding='utf-8')as r: txt = r.readlines()[0].split('.', 1)[1].strip()
        title = input(f"title应该是？直接回车为 {txt}") or txt
        s = f'|<b style="color: {color}">{name}</b>|[{title}](https://github.com/washing1127/LeetCode/blob/main/{name}/{name}.txt)|[python3](https://github.com/washing1127/LeetCode/blob/main/{name}/{name}.py)|'
        done_dic[name] = s
        # print(s)

text = """# LeetCode
The solutions of LeetCode questions.

## DoneList
|num|title|answer|
|:---:|:---:|---|\n"""
keys = list(done_dic.keys())
keys.sort()
for k in keys:
    text += done_dic[k] + '\n'

with open('README.md', 'w', encoding='utf-8')as w:
    w.write(text)