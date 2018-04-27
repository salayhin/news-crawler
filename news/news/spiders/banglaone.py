import scrapy
import pdb

class BanglaoneSpider(scrapy.Spider):
    name = "banglaone"

    def start_requests(self):
        urls = [
            'http://www.prothomalo.com/archive/2018-04-01?page=1',
            'http://www.prothomalo.com/archive/2018-04-01?page=2',
            'http://www.prothomalo.com/archive/2018-04-01?page=3',
            'http://www.prothomalo.com/archive/2018-04-01?page=4',
            'http://www.prothomalo.com/archive/2018-04-01?page=5',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_links = response.xpath("//div[contains(@class,'listing')]//div[contains(@class, 'each')]/a/@href").extract()

        for link in all_links:
            yield scrapy.Request(url=link, callback=self.get_details)

    def get_details(self, response):
        pdb.set_trace()
        news = response.xpath("")
        for city in cities[1:]:
            tr = Selector(text=city.encode('utf-8'), type="html")
            co_ordinate = tr.xpath("//tr/td[9]/small/span[contains(@class, 'plainlinks nourlexpansion')]/a/span[3]/span[1]/span[2]/span/text()").extract_first()

            yield {
                'city': self._find_city(city.encode('utf-8'), tr),
                'state': tr.xpath("//tr/td[3]/a/text()").extract_first(),
                'state_short_name': self._find_state_short_name(tr.xpath("//tr/td[3]/a/text()").extract_first()),
                'latitude': co_ordinate.split(';')[0],
                'longitude': co_ordinate.split(';')[1]
}
