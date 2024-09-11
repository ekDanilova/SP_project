import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_extension("***")

    browser = webdriver.Chrome(options=options)

    yield browser
    #print("\nquit browser..")
    #browser.quit()
