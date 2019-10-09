#!/usr/bin/python
# -*- coding:utf8 -*-


def get_city_country_population_1(city,country,population):
    """返回城市、国家及人口数量"""
    city_country_population = city.title() + ',' + country.title() + \
                              '-population ' + str(population)
    return city_country_population


def get_city_country_population_2(city,country,population=""):
    """返回城市，国家及人口"""
    if population:
        city_country_population = city.title() + ',' + country.title() + \
                              '-population ' + str(population)
        return city_country_population
    else:
        city_country = city.title() + ',' + country.title()
        return city_country