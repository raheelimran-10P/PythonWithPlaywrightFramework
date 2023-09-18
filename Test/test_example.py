import logging
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from Pages.demo_page import DemoPage

# Load environment variables from the .env file
load_dotenv()


def test_demo(page):

    demo_page = DemoPage(page)
    logging.info("Starting the test...")
    demo_page.navigate()
    demo_page.abc()

