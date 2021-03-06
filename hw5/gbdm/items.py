# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Selector


def validate_photo(value):
    if value[:2] == '//':
        return 'https:{0}'.format(value)
    return value


def get_prices(value):
    tag = Selector(text=value)
    result = {'name': tag.xpath('.//span//text()').extract_first(),
              'value': tag.xpath('//text()').extract_first().split()
    }
    result['value'] = float(''.join(result['value']))
    return result


def get_params(value):
    param_tag = Selector(text=value)
    key = param_tag.xpath('.//span[@class="item-params-label"]/text()').extract_first().split(':')[0]

    value = ' '.join(
        [itm for itm in param_tag.xpath('//li/text()').extract() if not itm.isspace()]
    )
    return key, value


class YoulaItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    author_url = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
    params = scrapy.Field()
    descriptions = scrapy.Field()
    price = scrapy.Field()




