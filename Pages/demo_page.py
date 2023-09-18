import os
from dotenv import load_dotenv
from playwright.sync_api import expect
import re
from TestData.test_data import TestData

# Load environment variables from the .env file
load_dotenv()

class DemoPage:

    def __init__(self, page):
        self.page = page
        self.get_started = page.get_by_role("link", name="Get started")  #click
        self.installation = page.get_by_role("heading", name="Installation")

    def navigate(self):
        self.page.goto(os.getenv("BASE_URL"))

    def abc(self):
        self.get_started.click(timeout=TestData.TIMEOUT_IN_MILLISECONDS)
        expect(self.installation).to_be_visible()  
        expect(self.page).to_have_title(re.compile("Playwright"))
        

    # def enter_password(self, password: str):
    #     self.page.fill('input[name="password"]', password)

    # def click_login_button(self):
    #     self.page.click('button[type="submit"]')

    
