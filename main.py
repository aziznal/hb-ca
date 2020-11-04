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


def get_total_page_num(bot):
    
    total_page_num = bot.get_total_comments_page_num()

    if total_page_num == -1:
        total_page_num = 1  # Loop adds one and ends after one cycle

    return int(total_page_num)


def save_collected_comments(filename, data, real_rating):
    """
    Take in a list of Comment objects and save it as csv
    """
    
    colnames = "author,author_rating,body,real_rating"

    with open( "scraped_data/"  + filename, "w", encoding="utf-8") as file:
        file.write(colnames + "\n")
        for comment in data:
            line = ",".join(list(comment.clean_soup.values()))
            line += "," + str(real_rating)
            file.write(line + "\n")


def run_program():
    
    filtered_data = pd.read_csv("notebook_data_comments50Plus.csv")

    product_titles = list(filtered_data['title'])
    product_urls = list(filtered_data['url'])
    product_ratings = list(filtered_data['rating'])

    comments = {}

    bot = hepsiBot(options=custom_options, is_product_page=False)

    for title, url, rating in zip(product_titles, product_urls, product_ratings):
        
        title = title.replace('"', '').replace("'", "").replace('/', '').replace('\\', '') # quotes and slashes break everything
        url += "-yorumlari"
        bot.goto(url)

        total_page_num = get_total_page_num(bot)

        comments[title] = []

        for i in range(2, total_page_num + 1):
            bot.mousewheel_vscroll(3)
            comments[title] += bot.scrape_comments()
            print("Scraped Page " + str(i - 1))
            bot.goto_next_comments_page(starting_url=url, next_page_num=i)
        
        print("\n")

        # for comment in comments[title]:
            # [print(f"{key}: {value}") for key, value in comment.clean_soup.items()]
            # print("_" * 70 + "\n")

        save_collected_comments(filename=title + ".csv", data=comments[title], real_rating=rating)

        print("\nSaved comments for " + title + "\n")


def extract_phones_w_100plus_comments():
    phone_data = pd.read_csv("./scraped_data/phone_thumbnails.csv") 

    filtered_data = phone_data[phone_data['comment_amount'] > 100]
    
    filtered_data.to_csv("phone_data_comments100Plus.csv")


if __name__ == "__main__":
    run_program()
    # extract_phones_w_100plus_comments()
