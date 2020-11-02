from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options
from unidecode import unidecode


FULL_PAGE_SCROLL = 10   # *Only an estimate


custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


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
