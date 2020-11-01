from basic_web_scraper.BasicSpider import BasicSpider
from DataStructures import ProductPage, Product, Thumbnail, Comment

from bs4 import BeautifulSoup


categories = {
    "laptop": "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
}


class hepsiBot(BasicSpider):
    def __init__(self, url, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        if url is not None:
            self.starting_url = url
        
        else:
            self.starting_url = self._browser.current_url

        self.current_page_num = self._infer_current_page_num()
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

    def _infer_current_page_num(self):
        
        current_url = self._browser.current_url

        if current_url == self.starting_url:
            return 1

        else:
            page_arg_index = current_url.find('sayfa')
            page_arg = current_url[page_arg_index:]

            page_arg_value = page_arg.split('=')[-1]

            return page_arg_value


    def goto_next_page(self):
        
        self.current_page_num = int(self._infer_current_page_num())

        if self.current_page_num < self.total_page_num:

            self.current_page_num += 1
            next_page_url = self.starting_url + "?sayfa=" + str(self.current_page_num)

            self.goto(next_page_url)

        else:
            raise Exception("Cannot goto next page. Already at final page")


    def get_all_products(self):
        pass
