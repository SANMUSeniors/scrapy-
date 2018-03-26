
import scrapy
class JiandanItem(scrapy.Item):
    title = scrapy.Field()#类别，用来生成存储目录
    image_urls = scrapy.Field()  # 图片的链接
    images = scrapy.Field()#自动生成的存储图片url，图片hash和checksum
