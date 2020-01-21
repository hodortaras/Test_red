import scrapy
from slugify import slugify
from .utils import str_to_float_join


class ProductSpider(scrapy.Spider):
    name = "parse_products"

    start_urls = [
        'https://bt.rozetka.com.ua/coffee_machines/c80164/',
    ]

    def parse(self, response):
        for product in response.css('div.goods-tile__inner'):
            yield {
                'name': product.css('img.lazy_img_hover::attr(alt)').get(),
                'slug': slugify(product.css('span.goods-tile__title::text').get()),
                'image': product.css('img.lazy_img_hover::attr(data-url)').get(),
                'price': str_to_float_join(product.css('span.goods-tile__price-value::text').get().split()),
                'description': 'lorem',
            }
        next_page = response.css('a.pagination__direction::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# response.css('ul.catalog-grid li.catalog-grid__cell_type_slim app-goods-tile-default div.goods-tile div.goods-tile__inner a.goods-tile__heading span.goods-tile__title::text').getall()
