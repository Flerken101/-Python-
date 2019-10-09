#!/usr/bin/python
# -*- coding:utf8 -*-


import pygal
import requests
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

def get_status_code():
    #调用API

    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    return r.status_code

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

get_status_code()