from hepsiBot import hepsiBot, categories
from selenium.webdriver.firefox.options import Options
from unidecode import unidecode

from functions import save_as_csv



def save_as_csv(data, col_names, filename, overwrite=False):
    """
    Take in data as a list of dictionaries
    and save it as a csv
    """

    column_names = ",".join(col_names)

    with open(filename, "w" if overwrite else "a") as file:
        file.write(column_names + "\n")

        for entry in data:
            for key in entry.keys():
                file.write(f"{unidecode(str(entry[key]))},")

            file.write('\n')


def scrape_category():
    """
    This method is here as a rough guide to how I scraped the notebook and phone categories
    """
    bot = hepsiBot(url=categories['phone'], options=custom_options)

    bot.wait()

    thumbnails = []

    for _ in range(bot.total_page_num):
        thumbnails += bot.get_all_products()
        try:
            bot.goto_next_page()
        
        except Exception as e:
            break;

    formatted_thumbnails = [thumbnail.clean_soup for thumbnail in thumbnails]
    column_names = ["instock", "title", "url", "comment_amount", "rating", "price"]

    save_as_csv(data=formatted_thumbnails, col_names=column_names, filename="phone_thumbnails.csv", overwrite=True)

