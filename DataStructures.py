from bs4 import BeautifulSoup


class DataStructure:
    def __init__(self, soup):
        """
        Superclass for all classes in this file.
        """
        self.soup = soup

        self.clean_soup = self.breakdown_soup()

    def breakdown_soup(self):
        raise Error("Unimplemented Superclass Method")


class ProductPage(DataStructure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a ProductPage (i.e Array of Products)
        """
        pass


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

    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a Product's Thumbnail (Price, Rating, Comments, etc..)
        """
        pass


class Comment(DataStructure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def breakdown_soup(self):
        """
        Return a dictionary of items relevant to a Comment (Author, Body, Rating, etc..)
        """
        pass
