# from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options
from unidecode import unidecode
import pandas as pd

# from functions import save_as_csv


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
    product_urls = list(filtered_data['url'])


    for url in product_urls:
        print("yo")



if __name__ == "__main__":
    run_program()
