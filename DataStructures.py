from bs4 import BeautifulSoup


class DataStructure:
    def __init__(self, soup):
        """
        Superclass for all classes in this file.
        """
        self.soup = soup

        self.clean_soup = self.breakdown_soup()

    def breakdown_soup(self):
        raise Exception("Unimplemented Superclass Method")


class Product(DataStructure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a Product (Price, Rating, etc..)
        """
        pass


class Thumbnail(DataStructure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def _check_instock(self):
        in_stock = self.soup.find('span', attrs={'class': 'out-of-stock-text'}) is None

        return in_stock

    def _extract_title(self):
        product_title = self.soup.find('h3', attrs={"class": "product-title"}).getText()

        product_title = product_title.replace('\n', '').strip()

        return product_title

    def _extract_url(self):
        product_url = self.soup.find("a")

        return "https://hepsiburada.com" + product_url['href']

    def _extract_comment_count(self):
        raw_comment_count = self.soup.find('span', attrs={"class": "number-of-reviews"})

        if raw_comment_count is not None:
            comment_count = int(raw_comment_count.getText()[1:-1])

        else:
            comment_count = 0

        return comment_count

    def _extract_rating(self):
        """
        If given product has no ratings then -1 will be returned
        """
        raw_rating = self.soup.find('span', attrs={"class": "ratings active"})

        if raw_rating is not None:
            rating = int(raw_rating['style'].split(':')[-1].strip().replace('%', '').replace(';', '')) / 20

        else:
            rating = -1

        return rating

    def _extract_price(self):
        
        raw_price = self.soup.find("span", attrs={"class": "price product-price"})
        
        if raw_price is not None:
            price = float(raw_price.getText().replace('.', '').replace(',', '.').split(' ')[0])

        else:
            raw_price = self.soup.find('div', attrs={"class": "price-value"})

            if raw_price is not None:
                price = float(raw_price.getText().strip().split(' ')[0].replace('.', '').replace(',', '.'))

            else:
                price="Not Available"
            

        return price

    def _extract_all(self):
        title = self._extract_title()
        url = self._extract_url()
        comment_count = self._extract_comment_count()
        rating = self._extract_rating()
        price = self._extract_price()


        return {
            "instock": True,
            "title": title,
            "url": url,
            "comment_count": comment_count,
            "rating": rating,
            "price": price
        }

    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a Product's Thumbnail (Price, Rating, Comments, etc..)
        """
        
        instock = self._check_instock()

        if instock:
            return self._extract_all()

        else:
            return { "instock": instock }


class Comment(DataStructure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def _extract_comment_author(self):
        raw_author = self.soup.find('div', attrs={'class': 'hermes-ReviewCard-module-1-Wp3'})

        author = ' '.join(raw_author.getText().strip().split())

        return author

    def _extract_author_rating(self):
        raw_rating = self.soup.find('div', attrs={'itemprop': 'reviewRating'})
        rating = raw_rating.find('span', attrs={'itemprop': 'ratingValue'})['content']
        return rating

    def _extract_comment_body(self):
        try:
            body = self.soup.find("div", attrs={"class": "hermes-ReviewCard-module-2dVP9"}).getText()
            body = ' '.join(body.split())   # To clear the crazy amount of spaces in the text
    
        except Exception as e:
            body = "NO_COMMENT"

        return body

    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a Comment (Author, Body, Rating, etc..)
        """
        
        comment_body = self._extract_comment_body()
        author = self._extract_comment_author()
        author_rating = self._extract_author_rating()

        return {
            "author": author,
            "author_rating": author_rating,
            "body": comment_body
        }



def test_thumbnail_class():
    
    with open('./raw_product_thumbnail.html', 'r') as html_file:
        raw_html = html_file.read()

    soup = BeautifulSoup(raw_html, features="lxml")

    thumby = Thumbnail(soup=soup)

    [print(f"{key}: {val}\n") for key, val in thumby.clean_soup.items()]


def test_comment_class():
    with open("product_comment_templates/raw_product_comment_page.html", "r", encoding="utf-8") as file:

        raw_html = file.read()

    soup = BeautifulSoup(raw_html, features="lxml")

    comment_container = soup.find("div", attrs={"class": "paginationContentHolder"})

    comments = comment_container.findChildren(recursive=False)

    for comment in comments:
        test_comment = Comment(comment)

        [print(f"{key}: {val}\n") for key, val in test_comment.clean_soup.items()]

        print("_"*75 + "\n")



if __name__ == "__main__":
    # test_thumbnail_class()

    test_comment_class()

