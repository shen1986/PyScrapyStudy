# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from FilmSpider.items import DyttFilmItem, FilmItemLoader
from FilmSpider.utils.common import get_md5


class FilmbtSpider(scrapy.Spider):
    name = 'filmBt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/']

    def parse(self, response):
        # 进到主页后找到新片精品的更多链接
        new_film_url = response.css('#header .bd3rl .co_area2 .title_all em a::attr(href)').extract_first("")

        film_url_list = response.css("#header .bd3rl  .co_area2 .inddline a:nth-child(2)")

        index = 0

        for film_url in film_url_list:
            url = film_url.css('::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)
            index = index + 1
            if index > 15:
                break

        # if new_film_url:
            # 跳转到新片精品第一页
            # yield Request(url=parse.urljoin(response.url, newFilm_url), callback=self.parse)

            # 直接爬取该页面内容

            # "//*[@id="header"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tbody/tr[2]/td[1]/a[2]"
        # else:
        #     """
        #     1. 获取电影列表页中的文章url并交给scrapy下载后并进行解析
        #     2. 获取下一页的url并交给scrapy进行下载
        #     """
            # 获取电影列表页中的文章url并交给scrapy下载后并进行解析
            # detail_url_list = response.css('#header .bd3r .co_area2 .co_content8 table a::attr(href)').extract()
            # for detail_url in detail_url_list:
            #     yield Request(url=parse.urljoin(response.url, detail_url), callback=self.parse_detail)

            # 提取下一页并交给scrapy进行下载
            # page_list = response.css('#header .x a')
            # for page in page_list:
            #     text = page.css('::text').extract_first("")
            #     if text == '下一页':
            #         next_page_url = page.css('::attr(href)').extract_first()
            #         yield Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse)
            #         break


    # 提取文章的具体字段
    def parse_detail(self, response):
        # 电影标题 发布时间 IMDb评分 豆瓣评分 图片 magnet ftp 正文内容
        item_loader = FilmItemLoader(item=DyttFilmItem(), response=response)
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("title", "#header .title_all h1 font::text")
        item_loader.add_css("magnet", "#Zoom p a::attr(href)")
        item_loader.add_css("publish_time", "#header .co_content8 ul::text")
        item_loader.add_css("content", "#Zoom p")
        item_loader.add_css("imdb_score", "#Zoom p")
        item_loader.add_css("douban_score", "#Zoom p")
        item_loader.add_css("ftp_address", "#Zoom table a::text")
        item_loader.add_css("front_image_url", "#Zoom img::attr(src)")

        film_item = item_loader.load_item()

        yield film_item
