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
from models.es_types import FilmType
from elasticsearch_dsl.connections import connections
es = connections.create_connection(FilmType._doc_type.using)


class FilmspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FilmItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()


def converTime(value):
    re_match = re.match('[\S\s]*?(\d+[-]\d+[-]\d+)[\S\s]*', value)

    if re_match:
        value = re_match.group(1)

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

def gen_suggests(index,info_tuple):
    # 根据字符串生成建议数组
    used_words = set()
    suggests = []
    if len(info_tuple) > 1:
        for text, weight in info_tuple:
            if text:
                # 调用es的analyze接口分析字符串
                words = es.indices.analyze(index=index,analyzer="ik_max_word",params={'filter':["lowercase"]}, body=text)
                anylyed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
                new_words = anylyed_words - used_words
            else:
                new_words = set()

            if new_words:
                suggests.append({"input":list(new_words), "weight": weight})
    else:
        text, weight = info_tuple
        if text:
            # 调用es的analyze接口分析字符串
            words = es.indices.analyze(index=index, analyzer="ik_max_word", params={'filter': ["lowercase"]}, body=text)
            anylyed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
            new_words = anylyed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input": list(new_words), "weight": weight})

    return suggests

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

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO film (title, publish_time, url, url_object_id,
            magnet, imdb_score,
            douban_score, ftp_address, content)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE content=VALUES(content), magnet=VALUES(magnet)
        """
        params = (self["title"], self["publish_time"], self["url"], self["url_object_id"],
                  self["magnet"], self["imdb_score"],self["douban_score"], self["ftp_address"], self["content"])

        return insert_sql, params

    def save_to_es(self):
        article = FilmType()
        article.url = self["url"]
        article.title = self["title"]
        article.magnet = self["magnet"]
        article.publish_time = self["publish_time"]
        article.content = self["content"]
        article.imdb_score = self["imdb_score"]
        article.douban_score = self["douban_score"]
        article.ftp_address = self["ftp_address"]
        # article.front_image_url = self["front_image_url"]
        # article.front_image_path = self["front_image_path"]
        article.meta.id = self["url_object_id"]

        article.suggest = gen_suggests(FilmType._doc_type.index,((article.title,10),(False, False)))

        article.save()
        return