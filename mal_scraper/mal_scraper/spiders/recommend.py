import scrapy
import re


class RecommendationSpider(scrapy.Spider):
    name = "recommendation"

    def start_requests(self):
        for i in range(0, 50000, 100):
            yield scrapy.Request(url=f"https://myanimelist.net/recommendations.php?s=recentrecs&t=anime&show={i}", callback=self.p2)

    def p2(self, response):
        string = ""
        for recommendation in response.xpath("//div[@class='spaceit borderClass']"):
            reason = "".join(recommendation.xpath("./div[@class='spaceit recommendations-user-recs-text']//text()").getall())
            anime = ";".join(recommendation.xpath('.//td/a/@href').getall())
            string += f"{anime}\n{reason}\n<end>\n\n"
        with open('./recommendations_full.txt', 'a+') as f:
            f.write(string)
