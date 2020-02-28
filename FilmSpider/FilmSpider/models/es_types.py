from datetime import  datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Double
from elasticsearch_dsl.connections import connections

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}

ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class FilmType(DocType):
    # 实现搜索建议
    suggest = Completion(analyzer=ik_analyzer)
    # 定义主要字段
    url = Keyword()
    title = Text(analyzer="ik_max_word")
    magnet = Keyword()
    publish_time = Date()
    content = Text(analyzer="ik_max_word")
    imdb_score = Double()
    douban_score = Double()
    ftp_address = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()

    class Meta:
        index = 'entertainment'
        doc_type = 'film'

if __name__ == "__main__":
    FilmType.init()