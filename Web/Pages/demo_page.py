import os
from dotenv import load_dotenv
from playwright.sync_api import expect
import re
from TestData.test_data import TestData

class DemoPage:

    def __init__(self, page):
        self.page = page
        self._get_started = page.get_by_role("link", name="Get started")  #click
        self._installation = page.get_by_role("heading", name="Installation")

    def navigate(self):
        self.page.goto(os.getenv("BASE_URL"))

    def installation(self):
        self._get_started.click(timeout=TestData.TIMEOUT_IN_MILLISECONDS)
        expect(self._installation).to_be_visible()  
        expect(self.page).to_have_title(re.compile("Playwright"))
        

    # def enter_password(self, password: str):
    #     self.page.fill('input[name="password"]', password)

    # def click_login_button(self):
    #     self.page.click('button[type="submit"]')

    
