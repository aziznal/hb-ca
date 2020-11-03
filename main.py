from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options
from unidecode import unidecode
import pandas as pd

from bs4 import BeautifulSoup

from functions import save_as_csv


FULL_PAGE_SCROLL = 10   # *Only an estimate

custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


def filter_notebook_data():
    data = pd.read_csv("scraped_data/notebook_thumbnails.csv", delimiter=",")
    data = data[data['price'] != "Not Available"]

    filtered_data = data[data['comment_amount'] > 50]    
    filtered_data['price'] = pd.to_numeric(filtered_data['price'], downcast="float")

    filtered_data.to_csv("notebook_data_comments50Plus.csv")


def run_program():
    
    filtered_data = pd.read_csv("notebook_data_comments50Plus.csv")

    product_titles = list(filtered_data['title'])
    product_urls = list(filtered_data['url'])

    comments = {}

    bot = hepsiBot(options=custom_options, is_product_page=False)

    for title, url in zip(product_titles, product_urls):
        
        title = title.replace('"', '').replace("'", "").replace('/', '').replace('\\', '') # replace quotes with nothing
        url += "-yorumlari"
        bot.goto(url)

        total_page_num = bot.get_total_page_num_product_page()

        comments[title] = []

        for i in range(2, total_page_num + 1):
            # comments[title] += bot.scrape_comments()
            print("Page" + str(i) + " has been scrooped")
            bot.goto_next_comments_page(starting_url=url, next_page_num=i)



if __name__ == "__main__":
    run_program()
