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
        
        headlinesections = response.css('div.headline-slider a.headline-slider-item')
        for headlinesection in headlinesections:
            yield {
                'title' : headlinesection.css('div.title ::text').get(),
                'url' : headlinesection.css('a').attrib['href']
            }
