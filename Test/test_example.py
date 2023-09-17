import re
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def test_has_title(page: Page):
    page.goto(os.getenv("BASE_URL"))

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()