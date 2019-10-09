#!/usr/bin/python
# -*- coding:utf8 -*-

def get_city_country(city,country):
    """返回城市及国家"""

    city = input("City: ")
    country = input("Country: ")
    city_country = city.title() + "," + country.title()
    return city_country