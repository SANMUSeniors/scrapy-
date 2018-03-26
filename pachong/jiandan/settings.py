
BOT_NAME = 'jiandan'
SPIDER_MODULES = ['jiandan.spiders']
NEWSPIDER_MODULE = 'jiandan.spiders'
ROBOTSTXT_OBEY = False
LOG_FILE  ="file_name"#日志文件
ITEM_PIPELINES = {'jiandan.pipelines.JiandanPipeline': 300,
  'jiandan.pipelines.ImagesPipeline':1,
}#开启两个管道
#ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE='f:\\onlylady'#设置自己的存储路径

#我在这里关闭缩略图功能了
'''IMAGES_THUMBS = {#缩略图的尺寸，设置这个值就会产生缩略图

    'small': (50, 50),

    'big': (200, 200),

}'''
