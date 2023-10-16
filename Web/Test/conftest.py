import pytest
from playwright.sync_api import Page

@pytest.fixture()
def set_up_tear_down(page: Page) -> None:

    page.set_viewport_size({"width": 1536, "height": 800})
    # page.goto("https://www.saucedemo.com")
    yield page

