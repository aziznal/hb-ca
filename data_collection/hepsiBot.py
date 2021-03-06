from basic_web_scraper.BasicSpider import BasicSpider
from DataStructures import Product, Thumbnail, Comment

from bs4 import BeautifulSoup
from unidecode import unidecode


categories = {
    "laptop": "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98",
    "phone": "https://www.hepsiburada.com/cep-telefonlari-c-371965"
}


class hepsiBot(BasicSpider):
    def __init__(self, url=None, is_product_page=True, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        if url is not None:
            self.starting_url = url
        
        else:
            self.starting_url = self._browser.current_url

        if is_product_page:
            self.current_page_num = self._infer_current_page_num()
            self.total_page_num = self._get_total_page_num()


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
            self.page_soup = BeautifulSoup(self._browser.page_source, features="lxml")

        else:
            raise Exception("Cannot goto next page. Already at final page")


    def _convert_to_product(self, raw_product):
        converted_product = Thumbnail(raw_product)
        return converted_product

    def _get_all_products(self, raw_products):
        """
        This method converts given product source code into a python object
        """

        converted_products = []

        for product in raw_products:
            converted_products.append(self._convert_to_product(product))

        return converted_products


    def get_all_products(self):
        """
        Grab all product thumbnails and returned their parsed version

        :returns: list[Thumbnail]
        """

        page_soup = BeautifulSoup(self._browser.page_source, features="lxml")

        products = page_soup.find_all("li", attrs={"class": "search-item"})

        return self._get_all_products(raw_products=products)

    
    def get_product_page_source(self):
        return self._browser.page_source


    def get_total_comments_page_num(self):
        pagination_element = self._browser.find_elements_by_class_name("hermes-PaginationBar-module-3qhrm")
        
        if pagination_element is not None and len(pagination_element) > 0:
            pagination_soup = BeautifulSoup(pagination_element[0].get_attribute("innerHTML"), features="lxml")

            page_num = pagination_soup.findAll("li")[-1].getText()

        else:
            page_num = -1

        return int(page_num)

    def goto_next_comments_page(self, starting_url, next_page_num):
        next_page_url = starting_url + "?sayfa=" + str(next_page_num)
        self.goto(next_page_url)

    def _get_comment_body(self, comment_body):
        return Comment(comment_body)

    def scrape_comments(self):
        """
        :returns: List[Comment]
        """

        soup = BeautifulSoup(self._browser.page_source, features="lxml")

        comment_container = soup.find('div', attrs={'class': 'paginationContentHolder'})

        raw_comments = comment_container.findChildren(recursive=False)

        comments = [self._get_comment_body(comment) for comment in raw_comments]

        return comments