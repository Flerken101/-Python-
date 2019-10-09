#!/usr/bin/python
# -*- coding:utf8 -*-

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

def get_status_code():
    return r.status_code

#将API响应存储到一个变量中
response_dict = r.json()

def get_repos_number():
    return response_dict['total_count']

#研究有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]

def get_repos_returned_number():
    repos_returned_number = len(repo_dict)
    return repos_returned_number

for key in sorted(repo_dict.keys()):
    print(key)
