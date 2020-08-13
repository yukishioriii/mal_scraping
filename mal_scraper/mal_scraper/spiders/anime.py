import scrapy
import re


class AnimeSpider(scrapy.Spider):
    name = "anime"

    def start_requests(self):
        for i in range(3000, 5000, 50):
            yield scrapy.Request(url=f"https://myanimelist.net/topanime.php?limit={i}", callback=self.p1)

    def p1(self, response):
        urls = response.xpath(
            "//tr[@class='ranking-list']//a[@class='hoverinfo_trigger fl-l fs14 fw-b']/@href").getall()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.p2)

    def p2(self, response):
        name = response.url
        desc = re.sub('\n', '', "".join(response.xpath(
            "//span[@itemprop='description']//text()").getall()))
        with open('./anime2.txt', 'a+') as f:
            f.write(f"{name}\n{desc}\n<end>\n\n")
