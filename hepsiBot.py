from basic_web_scraper.BasicSpider import BasicSpider
from DataStructures import ProductPage, Product, Thumbnail, Comment


class hepsiBot(BasicSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def at_page_bottom(self):
        """
        Return true if bot has reached the bottom of the page
        """
        pass


    def goto_next_page(self):
        pass

    def goto_prev_page(self):
        pass


    def get_all_products(self):
        pass
