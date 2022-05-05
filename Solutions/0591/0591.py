# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/2 10:40
# File: 0591.py
# Desc: 


class Solution:
    def isValid(self, code: str) -> bool:
        tag_name = re.match("<[A-Z]{1,9}>", code)
        if not tag_name: return False
        tag_name = tag_name.group()
        if not code.endswith("</"+tag_name[1:]): return False
        tag_content = code[len(tag_name):-len(tag_name)-1]
        # print(tag_content,'\n')
        # print(re.search("<!\[CDATA\[.*?\]\]>", tag_content))
        tag_content = re.sub("<!\[CDATA\[.*?\]\]>", "a", tag_content)
        while s:=re.search("<[A-Z]{1,9}>", tag_content):
            subname = s.group()
            # print(subname)
            idx = tag_content.rfind(subname)
            # flag = False
            # for subs in re.findall(s.group()+".*?</"+s.group()[1:], tag_content[idx]):
                # print(subs)
                # if self.isValid(subs):
                    # print(subs)
                    # flag = True
                    # break
            subs = re.search(subname+".*?</"+subname[1:], tag_content[idx:])
            if not subs: return False
            # print(subs.group(), '=====')
            if not self.isValid(subs.group()): return False
            # if not flag: return False
            tag_content = tag_content.replace(subs.group(), '')
        return "<" not in tag_content
