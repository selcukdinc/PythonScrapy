# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


def serialize_price(value):
    return f'$ {str(value)}'



class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    num_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    


'''
    'url' : response.url,
    'title' : response.css('.product_main h1::text').get(),
    'product_type' : table_rows[1].css('td::text').get(),
    'price_excl_tax' : table_rows[2].css('td::text').get(),
    'price_incl_tax' : table_rows[3].css('td::text').get(),
    'tax' : table_rows[4].css('td::text').get(),
    'availability' : table_rows[5].css('td::text').get(),
    'num_reviews' : table_rows[6].css('td::text').get(),
    'stars' : response.css("p.star-rating").attrib['class'],
    'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
    'description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
    'price' : response.css('p.price_color ::text').get()
'''