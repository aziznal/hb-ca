from basic_web_scraper.BasicSpider import BasicSpider
from DataStructures import ProductPage, Product, Thumbnail, Comment

from bs4 import BeautifulSoup


categories = {
    "laptop": "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
}


class hepsiBot(BasicSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.total_page_num = self._get_total_page_num()

    def at_page_bottom(self):
        """
        Return true if bot has reached the bottom of the page
        """
        pass


    def _get_total_page_num(self):
        pagination_id = "pagination"
        pagination_element = self._browser.find_element_by_id(id_="pagination")

        soup = BeautifulSoup(pagination_element.get_attribute("innerHTML"), "lxml")

        pagination_list = soup.findChildren(name="li", recursive=True)
        
        page_num = int(pagination_list[-1].findChildren("a")[0].getText())

        return page_num


    def goto_next_page(self):
        pass

    def goto_prev_page(self):
        pass


    def get_all_products(self):
        pass
