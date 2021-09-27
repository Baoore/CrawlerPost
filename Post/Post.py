# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
import urllib
from slugify import slugify
import calendar;
import time;

def remove_tags_serializer(value):
    return remove_tags(value)

def save_image_serializer(value):
    try:
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        image_on_web = urllib.request.urlopen(value)
        meta = image_on_web.info()

        if meta["content-type"] in image_formats and image_on_web.getcode() == 200:
            buf = image_on_web.read()
            file_path = "/var/www/africaninterest/public_html/storage/app/uploads/public/" + str(calendar.timegm(time.gmtime())) +"."+ meta["content-type"].rsplit('/', 1)[1]
            downloaded_image = open(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
            print(file_path)
        else:
            return ""
    except:
        return ""

class Post(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field(serializer = remove_tags_serializer)
    author = scrapy.Field(serializer = remove_tags_serializer)
    content = scrapy.Field(serializer = remove_tags_serializer)
    content_html = scrapy.Field()
    source_scraped = scrapy.Field()
    category_scraped = scrapy.Field(serializer = remove_tags_serializer)
    scraped_at_timestamp = scrapy.Field(serializer=str)
    country_scraped = scrapy.Field()
    newly_scraped = scrapy.Field()
    source_url = scrapy.Field()
    published_date = scrapy.Field()
    featured_image = scrapy.Field(serializer = save_image_serializer)
