# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de producto
    producto_id = scrapy.Field()
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    material = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    disponibles = scrapy.Field()
    vendidos = scrapy.Field()
    opiniones = scrapy.Field()
    numero_opiniones = scrapy.Field()
    url_producto = scrapy.Field()
    categoria = scrapy.Field()

    #imagenes
    image_urls = scrapy.Field()
    image_name = scrapy.Field()

    #info de la tienda o vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
