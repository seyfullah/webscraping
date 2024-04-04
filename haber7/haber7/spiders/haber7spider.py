import scrapy


class Haber7spiderSpider(scrapy.Spider):
    name = "haber7spider"
    allowed_domains = ["www.haber7.com"]
    start_urls = ["https://www.haber7.com"]

    def parse(self, response):
        subheaders = response.css('div.subhead-slider a')
        
        for subheader in subheaders:
            yield {
                'title' : subheader.css('div.title ::text').get(),
                'url' : subheader.css('a').attrib['href']
            }
