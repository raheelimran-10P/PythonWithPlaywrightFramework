import logging
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv
from Pages.demo_page import DemoPage

# Load environment variables from the .env file ay the root of the project
is_env_file_loaded = load_dotenv()
if not is_env_file_loaded: 
    raise FileNotFoundError(".env file was not found! or not exist is a root directory")


def test_demo_01(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_page = DemoPage(page)
    logging.info("Starting the test...")
    demo_page.navigate()
    demo_page.installation()

def test_demo_02(set_up_tear_down) -> None:
    pass

