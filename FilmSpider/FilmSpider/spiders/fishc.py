# -*- coding: utf-8 -*-
import scrapy
try:
    import urlparse as parse
except:
    from urllib import parse

class FishcSpider(scrapy.Spider):
    name = 'fishc'
    allowed_domains = ['https://fishc.com.cn/']
    start_urls = ['https://fishc.com.cn/thread-51842-1-1.html']

    headers = {
        "HOST": "fishc.com.cn",
        "Referer": "https://fishc.com.cn/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
    }

    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def parse(self, response):
        """
        提取出html页面中的所有url 并跟踪这些url进行一步爬取
        如果提取的url中格式为 /question/xxx 就下载之后直接进入解析函数
        """
        all_urls = response.css("table a::attr(href)").extract()
        all_urls = list([parse.urljoin(response.url, url) for url in all_urls])
        all_urls = list(filter(lambda x: True if x.startswith("https") else False, all_urls))
        print(all_urls)
        # all_urls = [parse.urljoin(response.url, url) for url in all_urls]
        # all_urls = filter(lambda x:True if x.startswith("https") else False, all_urls)

        pass

    # 登录
    def start_requests(self):
        post_url = "https://fishc.com.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        post_data = {
            "username": "shen1986",
            "password": "4456d776d1c73dddaa25d88b317ace7b",
            "quickforward": "yes",
            "handlekey": "ls"
        }

        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        if response.status == 200:
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)

