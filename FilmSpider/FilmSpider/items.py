# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from FilmSpider.utils.common import get_md5


class FilmspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FilmItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()


def converTime(value):
    try:
        publish_time = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except Exception as e:
        publish_time = datetime.datetime.now().date()
    return publish_time


def getContent(value):
    re_match = re.match('(.*)[<]strong[>][<]font color.*', value)

    if re_match:
        value = re_match.group(1)

    return value


def getImdbScore(value):
    re_match = re.match('.*IMDb评分.*?(\d+[.]?\d{0,1}).*', value)

    if re_match:
        imdb_score = re_match.group(1)
    else:
        imdb_score = 0

    return imdb_score


def getDoubanScore(value):
    re_match = re.match('.*豆瓣评分.*?(\d+[.]?\d{0,1}).*', value)

    if re_match:
        douban_score = re_match.group(1)
    else:
        douban_score = 0

    return douban_score


def getUrl(value):
    return value


class DyttFilmItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field(
        input_processor=MapCompose(get_md5)
    )
    title = scrapy.Field()
    magnet = scrapy.Field()
    publish_time = scrapy.Field(
        input_processor=MapCompose(converTime)
    )
    content = scrapy.Field(
        input_processor=MapCompose(getContent)
    )
    imdb_score = scrapy.Field(
        input_processor=MapCompose(getImdbScore)
    )
    douban_score = scrapy.Field(
        input_processor=MapCompose(getDoubanScore)
    )
    ftp_address = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(getUrl)
    )
    front_image_path = scrapy.Field()