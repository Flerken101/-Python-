#!/usr/bin/python
# -*- coding:utf8 -*-

#17.1 使用Web API
#17.1.1 Git和Github
#17.1.2 使用API调用请求数据
#17.1.3 安装requests
#17.1.4 处理API响应

import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应储存在一个变量中
response_dict = r.json()

#处理结果
print(response_dict.keys())

#17.1.5 处理响应字典
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nkeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

##提取repo_dict中与一些键相关的值
import io
import sys
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\nName:", repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print("Description:",repo_dict['description'])

#17.1.6概述最受欢迎的仓库
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print("Description:", repo_dict['description'])

#17.1.7 监视API的速率限制


#17.2 使用Pygal可视化仓库
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')

#17.2.1改进Pygal图表


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
request = requests.get(url)
print("Status code:",request.status_code)

#将API响应存储在变量中
r = request.json()

#探索有关仓库的信息
repo_dicts = r['items']

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style = RS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Started Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('Python_repos.svg')

#17.2.2 添加自定义工具提示

import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

my_style = RS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [
    {'value':16101,'label':'Description of httpie'},
    {'value':15028, 'label': 'Description of django'},
    {'value':14798, 'label': 'Description of flask'}
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')

#17.2.3 根据数据绘图

import pygal
import requests
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

#调用API

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)

#将API响应存储到变量中
request = r.json()

#探索仓库的有关信息
repo_dicts = request['items']
print("Number of items:",len(repo_dicts))

names,plot_dicts =[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
    }

    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Started Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('Python_repos.svg')

#17.2.4 在图表中添加可单击的链接
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

#调用API

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)

#将API响应存储到变量中
request = r.json()

#探索仓库的有关信息
repo_dicts = request['items']
print("Number of items:",len(repo_dicts))

names,plot_dicts =[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url']
    }

    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Started Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('Python_repos.svg')

#17.3 Hacker News API

import requests
from operator import itemgetter

#执行API调用并响应存储
url = 'https://hacker-news.firebaseio.com/v0/item/topstories.json'
r = requests.get(url)
print("Status code:",r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:

    #对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) +
           '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments':response_dict.get('descendants',0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),
            reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:',submission_dict['title'])
    print("Discussion link:",submission_dict['link'])
    print("Comments:",submission_dict['comments'])

