from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options


FULL_PAGE_SCROLL = 10   # *Only an estimate


custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


def run_program():
    bot = hepsiBot(url=categories['laptop'], options=custom_options)

    bot.wait()

    for thumbnail in bot.get_all_products():
        print("\n")
        [print(f"{key}: {value}\n") for key, value in thumbnail.clean_soup.items()]
        print("\n")


if __name__ == "__main__":
    run_program()
