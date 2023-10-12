import logging
from dotenv import load_dotenv
from Web.Pages.demo_qa_page import DemoQaPage
from Web.TestData.test_data import TestData

# Load environment variables from the .env file ay the root of the project
# used any sensitive information like PASSWORD=os.getenv("PASSWORD")
is_env_file_loaded = load_dotenv()
if not is_env_file_loaded: 
    raise FileNotFoundError(".env file was not found! or not exist is a root directory")

def test_demo_01(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    demo_qa_page.text_box_activity()


