from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options

custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


def run_program():
    bot = hepsiBot(url=categories['laptop'], options=custom_options)

    bot.goto(categories['laptop'] + "?sayfa=23")

    bot.goto_next_page()


if __name__ == "__main__":
    run_program()
