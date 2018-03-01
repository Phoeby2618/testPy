# 思路：创建5个模块，html下载器，html解析器，url管理器，主函数，输出结果

# 在主函数入口处初始化爬取网页入口，和各个模块
from baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 在构造函数中初始化函数对象
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutput()

    # 循环爬取
    # ###学习模块，面向对象思想！用函数表达，再去编写具体的函数模块内容

    # 思路：首先添加入口url，
    # 当还有url时，从url库中选取一条新的url，下载url内容，用解析器解析内容，
    # 将解析出来的新url重新加到url中，将解析出的内容收集起来，最后输出
    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print('craw %d:%s' % (count,new_url))
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count==10:
                    break
                count+=1

            except:
                print('craw failed')

        self.outputer.output_html()



if __name__=='__main__':
    root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)