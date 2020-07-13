import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from MLM-scrappy.dispensador-item import MercadoItem

class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	allowed_domain = ['listado.mercadolibre.com.mx', 'hogar.mercadolibre.com.mx', '']
	start_urls = ['https://hogar.mercadolibre.com.mx/cocinas/bombas-bidones/']

	rules = {
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class="andes-pagination__link prefetch"]'))),
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="item__title list-view-item-title"]')), callback = 'parse_item', follow = False)
	}


	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		ml_item['producto_id'] = response.xpath('normalize-space(//span[@class="item-info__id-number"]/text())').extract_first()
		ml_item['titulo'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[2]/div[1]/section[1]/div/header/h1/text())').extract_first()
		ml_item['modelo'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[1]/section[2]/div/section[1]/ul/li[2]/span/text())').extract()
		ml_item['marca'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[1]/section[2]/div/section[1]/ul/li[1]/span/text())').extract()
		ml_item['material'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[1]/section[2]/div/section[2]/ul/li/span/text())').extract()
		ml_item['precio'] = response.xpath('normalize-space(//fieldset/span/span[@class="price-tag-fraction"]/text())').extract()
		ml_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		ml_item['disponibles'] = response.xpath('normalize-space(//span[@class="dropdown-quantity-available"]/text())').extract()
		ml_item['vendidos'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		ml_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		ml_item['numero_opiniones'] = response.xpath('normalize-space(//div[@class="review-summary-average-legend"]/text())').extract()
		ml_item['categoria'] = response.xpath('normalize-space(/html/body/main/section[2]/nav/div[1]/ul/li[3]/a/text())').extract()
		ml_item['url_producto'] = response.request.url
		ml_item['full'] = response.xpath('s')

		#imagenes del producto
		ml_item['image_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
		ml_item['image_name'] = response.xpath('normalize-space(/html/body/main/div/div[1]/div[2]/div[1]/section[1]/div/header/h1/text())').extract_first()
		
		#info de la tienda o vendedor
		ml_item['vendedor_url'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
		ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "card-subtitle section-subtitle power-seller")]/text())').extract()
		ml_item['ventas_vendedor'] = response.xpath('normalize-space(//dd[@class="reputation-relevant"]/strong/text())').extract()
		self.item_count += 1
		if self.item_count > 5:
			raise CloseSpider('item_exceeded')
		yield ml_item
