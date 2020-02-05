# -*- coding: utf-8 -*-
import scrapy
import re


class FilmbtSpider(scrapy.Spider):
    name = 'filmBt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/20200202/59664.html']

    def parse(self, response):
        # 电影标题 发布时间 IMDb评分 豆瓣评分 图片 magnet ftp
        title = response.xpath('//*[@id="header"]/div/div[3]/div[3]/div[1]/div[2]/div[1]/h1/font/text()').extract()[0]
        magnet = response.css('#Zoom p a::attr(href)').extract()[0]
        publish_time = response.xpath('//*[@id="header"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/ul/text()').extract()[0]


        print("aa")
        pass


# <div id="Zoom">
# <!--Content Start--><span style="FONT-SIZE: 12px"></span><td>
# <p><img border="0" src="https://extraimage.net/images/2020/02/02/929e3a29311b82d02c3e949b2fa8a206.jpg" alt=""> <br><br>◎译　　名　极速车王/地狱驾驶/极速之王/极速传奇：褔特决战法拉利(港)/福特大战法拉利/赛道狂人(台) <br>◎片　　名　Ford v Ferrari/Go Like Hell/Kings of the Road/Le Mans '66 <br>◎年　　代　2019 <br>◎产　　地　美国,法国 <br>◎类　　别　剧情 / 传记 / 运动 <br>◎语　　言　英语,意大利语,法语,日语 <br>◎字　　幕　中英双字幕 <br>◎上映日期　2019-08-30(特柳赖德电影节) / 2019-11-15(美国) <br>◎IMDb评分 8.2/10 from 107423 users <br>◎豆瓣评分　8.5/10 from 39,931 users <br>◎文件格式　x264 + aac <br>◎视频尺寸　1920 x 1080 <br>◎文件大小　2.54 GB <br>◎片　　长　152分钟 <br>◎导　　演　詹姆斯·曼高德 James Mangold <br>◎编　　剧　杰斯·巴特沃斯 Jez Butterworth <br>　　　　 　约翰-亨利·巴特沃斯 John-Henry Butterworth <br>　　　　 　贾森·凯勒 Jason Keller <br>　　　　 　A·J·拜梅 A.J. Baime <br>◎主　　演　马特·达蒙 Matt Damon <br>　　　　 　克里斯蒂安·贝尔 Christian Bale <br>　　　　 　乔·博恩瑟 Jon Bernthal <br>　　　　 　诺亚·尤佩 Noah Jupe <br>　　　　 　玛丽萨·佩特罗 Marisa Petroro <br>　　　　 　凯特瑞娜·巴尔夫 Caitriona Balfe <br>　　　　 　乔什·卢卡斯 Josh Lucas <br>　　　　 　雷·迈克金农 Ray McKinnon <br>　　　　 　约翰·约瑟夫·菲尔德 JJ Feild <br>　　　　 　崔西·莱茨 Tracy Letts <br>　　　　 　华莱士·朗翰 Wallace Langham <br>　　　　 　乔纳森·拉帕格里拉 Jonathan LaPaglia <br>　　　　 　斯特凡 Stefania Spampinato <br>　　　　 　鲁道夫·马丁 Rudolf Martin <br>　　　　 　拉奇兰·布坎南 Lachlan Buchanan <br>　　　　 　瓦德·霍尔顿 Ward Horton <br>　　　　 　肖恩·卡里甘 Sean Carrigan <br>　　　　 　克里斯托弗·达尔加 Christopher Darga <br>　　　　 　亚当·梅菲尔德 Adam Mayfield <br>　　　　 　乔瓦尼索罗菲瓦 Giovanni Cirfiera <br>　　　　 　乔·威廉森 Joe Williamson <br>　　　　 　本杰明·里格比 Benjamin Rigby <br>　　　　 　杰克·麦克马伦 Jack McMullen <br>　　　　 　保罗·福克斯 Paul Fox <br>　　　　 　雷莫·吉罗内 Remo Girone <br>　　　　 　德鲁·劳施 Drew Rausch <br>　　　　 　朱利安·米勒 Julian Miller <br>　　　　 　艾拉姆·奥里安 Aylam Orian <br>　　　　 　埃姆利·贝赫什蒂 Emil Beheshti <br>　　　　 　蒂芙妮·伊冯娜·考克斯 Tiffany Yvonne Cox <br>　　　　 　达林·库珀 Darin Cooper <br>　　　　 　科拉多·因韦尔尼齐 Corrado Invernizzi <br>　　　　 　特洛伊·迪林格 Troy Dillinger <br>　　　　 　彼得·阿佩塞拉 Peter Arpesella <br>　　　　 　斯凯勒·马歇尔 Skyler Marshall <br><br>◎标　　签　赛车 | 传记 | 美国 | 真实事件改编 | 剧情 | 2019 | 运动 | 动作 <br><br>◎简　　介 <br><br>　　基于真实故事，聚焦由汽车设计师卡罗尔·谢尔比带领的一队美国工程师、设计师，以及他旗下的英国车手肯·迈尔斯，亨利·福特二世要求谢尔比打造一辆全新的赛车，希望能在1966年的勒芒世界锦标赛上打败长期占主导地位的法拉利。最终福特GT40在勒芒24小时耐力赛中成功击败法拉利，并蝉联了1967和1968年的冠军。 <br><br>◎获奖情况 <br><br>　　第92届奥斯卡金像奖 (2020) <br>　　最佳影片(提名) <br>　　最佳剪辑(提名) 迈克尔·麦卡斯克/安德鲁·巴克兰 <br>　　最佳混音(提名) DavidGiammarco/史蒂文·莫罗/保罗·马瑟 <br>　　最佳音效剪辑(提名) <br>　　 <br>　　第77届金球奖 (2020) <br>　　电影类剧情片最佳男主角(提名) 克里斯蒂安·贝尔 <br>　　 <br>　　第73届英国电影学院奖 (2020) <br>　　电影奖最佳摄影(提名) 芬顿·帕帕迈可 <br>　　电影奖最佳剪辑(提名) 迈克尔·麦卡斯克/安德鲁·巴克兰 <br>　　电影奖最佳音效(提名) <br>　　 <br>　　第26届美国演员工会奖 (2020) <br>　　电影奖最佳男主角(提名) 克里斯蒂安·贝尔 <br>　　电影最佳特技群戏(提名) <br>　　 <br>　　第31届美国制片人工会奖 (2020) <br>　　最佳电影制片人奖(提名) <br>　　 <br>　　第34届美国摄影协会奖 (2020) <br>　　电影长片最佳摄影(提名) 芬顿·帕帕迈可 <br>　　 <br>　　第70届美国剪辑工会奖 (2020) <br>　　剧情片最佳剪辑(提名) 迈克尔·麦卡斯克/安德鲁·巴克兰 <br>　　 <br>　　第24届美国艺术指导工会奖 (2020) <br>　　电影奖最佳历史电影艺术指导(提名) 弗朗索瓦·奥杜伊 <br>　　 <br>　　第67届美国音效剪辑协会奖 (2020) <br>　　金卷轴奖最佳电影音效剪辑 <br>　　金卷轴奖最佳电影对白剪辑(提名) <br>　　 <br>　　第18届美国视觉效果协会奖 (2020) <br>　　最佳电影辅助视觉效果(提名) <br>　　 <br>　　第56届美国声音效果协会奖 (2020) <br>　　真人电影最佳音效 <br>　　 <br>　　第91届美国国家评论协会奖 (2019) <br>　　年度佳片 <br>　　 <br>　　第25届美国评论家选择电影奖 (2020) <br>　　最佳影片(提名) <br>　　最佳动作片(提名) <br>　　最佳摄影(提名) <br>　　最佳剪辑(提名) <br>　　最佳视觉效果(提名) <br>　　 <br>　　第24届金卫星奖 (2020) <br>　　电影部门最佳剧情片(提名) <br>　　电影部门最佳导演 詹姆斯·曼高德 <br>　　电影部门剧情片最佳男主角 克里斯蒂安·贝尔 <br>　　电影部门最佳原创剧本(提名) 杰斯·巴特沃斯/约翰-亨利·巴特沃斯/贾森·凯勒 <br>　　电影部门最佳原创配乐(提名) <br>　　电影部门最佳摄影(提名) <br>　　电影部门最佳视觉效果(提名) <br>　　电影部门最佳剪辑 <br>　　电影部门最佳音效 <br>　　电影部门最佳美术指导(提名) <br>　　 <br>　　第23届好莱坞电影奖 (2019) <br>　　年度导演 詹姆斯·曼高德 <br>　　年度剪辑 迈克尔·麦卡斯克/安德鲁·巴克兰 <br>　　年度音效 DavidGiammarco/DonaldSylvester/史蒂文·莫罗/保罗·马瑟 <br>　　 <br>　　第18届华盛顿影评人协会奖 (2019) <br>　　最佳剪辑 <br>　　 <br>　　第40届伦敦影评人协会奖 (2020) <br>　　年度英国/爱尔兰小演员(提名) 诺亚·尤佩 <br>　　 <br>　　第23届美国在线影评人协会奖 (2020) <br>　　最佳剪辑(提名) 迈克尔·麦卡斯克/安德鲁·巴克兰 <br><br><strong><font color="#ff0000"><font size="4">【下载地址】</font></font></strong> <br><br><br><a href="magnet:?xt=urn:btih:27b9926b44cbfcd883b0a485f30196d88a56768b&amp;dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1www.ygdy8.com.%e6%9e%81%e9%80%9f%e8%bd%a6%e7%8e%8b.BD.1080p.%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97%e5%b9%95.mkv&amp;tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&amp;tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&amp;tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce"><strong><font style="BACKGROUND-COLOR: #ff9966"><font color="#0000ff"><font size="4">磁力链点击 极速车王.BD.1080p.中英双字幕.mkv</font></font></font></strong></a></p>
# <p> </p>
# <p>
# </p><table style="BORDER-BOTTOM: #cccccc 1px dotted; BORDER-LEFT: #cccccc 1px dotted; TABLE-LAYOUT: fixed; BORDER-TOP: #cccccc 1px dotted; BORDER-RIGHT: #cccccc 1px dotted" border="0" cellspacing="0" cellpadding="6" width="95%" align="center">
#     <tbody>
#         <tr>
#             <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="ftp://ygdy8:ygdy8@yg18.dydytt.net:8005/%E9%98%B3%E5%85%89%E7%94%B5%E5%BD%B1www.ygdy8.com.%E6%9E%81%E9%80%9F%E8%BD%A6%E7%8E%8B.BD.1080p.%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97%E5%B9%95.mkv">ftp://ygdy8:ygdy8@yg18.dydytt.net:8005/阳光电影www.ygdy8.com.极速车王.BD.1080p.中英双字幕.mkv</a></td>
#         </tr>
#     </tbody>
# </table>
#  <br><center></center>
#
#
#
#
# </td>
#
#       </div>