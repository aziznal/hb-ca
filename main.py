from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options
from unidecode import unidecode

from functions import save_as_csv


FULL_PAGE_SCROLL = 10   # *Only an estimate


custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


def run_program():
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


if __name__ == "__main__":
    run_program()
