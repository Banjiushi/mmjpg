下边的工作环境是：
```
Python 3.6.2
windows 10
```  

准备工作：
> 首先准备一个放置你项目的目录（如：E:\spider\mmjpg）  
> 接着在控制台中进入该目录，并执行：   
> ```
> python -m venv env-mm
>  ```   
> 命令来创建一个虚拟环境（推荐），后边的工作都将在该虚拟环境中展开  
> **接下来：**  
> ```
> env-mm\Scripts\activate			# 激活环境
> pip install scrapy	# 安装 Scrapy，如果因为源而安装失败可以使用 pip install -i https://mirrors.aliyun.com/pypi/simply scrapy 安装
> pip install pypiwin32 	# 安装依赖，否则会报 ImportError: No module named win32api
> ```  
> 至此准备工作结束！

### 现在真正开始项目：
```
scrapy startproject  mm 	# 创建爬虫项目
scrapy genspider mmjpg "mmjpg.com"		# 创建爬虫，创建在 E:\spider\mmjpg\mm\mm\spiders 文件夹中
```   
编辑 `items.py`：

```
class MmItem(scrapy.Item):
    # 我们需要遍历网页所有套图，拿到套图 url 和标题就可以了
    title = scrapy.Field()
    url = scrapy.Field()
 ```
编辑 `spiders\mmjpg.py`：
```
class MmjpgSpider(scrapy.Spider):
    name = 'mmjpg' # 爬虫名
    allowed_domains = ['mmjpg.com'] # 可选，保证我们的爬虫只爬该域名下的网页
    base_url = 'http://www.mmjpg.com/home/'
    start_urls = [base_url + str(1)] # 修改到我们要使用的

    def parse(self, response):
        item = MmItem()
        pics = response.xpath("//div[@class='pic']//span/a/@href")
        title = response.xpath("//div[@class='pic']//span/a/text()")
        for pic in pics:
            item['url'] = pic.extract()
        for x in title:
            item['title'] = x.extract()

        yield item
```
编辑 `pipelines.py`：
```

```