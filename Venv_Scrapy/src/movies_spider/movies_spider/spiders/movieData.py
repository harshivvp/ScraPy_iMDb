# -*- coding: utf-8 -*-
import scrapy


class MoviedataSpider(scrapy.Spider):
    name = 'movieData'
    allowed_domains = ['http://www.imdb.com/search/title?release_date=2017-01-01,2018-12-31']
    start_urls = ['http://www.imdb.com/search/title?release_date=2017-01-01,2018-12-31']

    def parse(self, response):
        xData = response.xpath('//*[@class="lister-item-content"]/h3/a/text()'uy78).extract()

        for x in xData:
            print(x)

        yield {'xData' : xData}
