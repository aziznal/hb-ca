from hepsiBot import hepsiBot, categories

from selenium.webdriver.firefox.options import Options
from unidecode import unidecode

from functions import save_as_csv


FULL_PAGE_SCROLL = 10   # *Only an estimate


custom_options = Options()
custom_options.set_preference("dom.webnotifications.enabled", "false")
custom_options.set_preference("permissions.default.image", 2)


def run_program():
    pass

if __name__ == "__main__":
    run_program()
