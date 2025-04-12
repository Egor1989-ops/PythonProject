from selenium.webdriver import Remote
import pytest

from selenium.webdriver.chrome.options import options

@pytest.fixture()
def set_up_browser():
    options = Options()
    options.page.load_strategy = 'normal'
    driver = Remote(
        disared_capabilities={
            "browserName": "chrome"
            "broserVersion": "laters"
        },
        command_executor="http://127.0.0.1:4444/wd/hub"
        options=options
    )
    yield driver
    driver.quit()
