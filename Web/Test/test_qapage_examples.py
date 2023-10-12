import logging
from dotenv import load_dotenv
from Web.Pages.demo_qa_page import DemoQaPage
from Web.TestData.test_data import TestData
from Web.Util.DownloadsPathFinder import DownloadsPathFinder
from Web.Util.random_paragraph_util import RandomParagraphGenerator
import os
import time

# Load environment variables from the .env file ay the root of the project
# used any sensitive information like PASSWORD=os.getenv("PASSWORD")
is_env_file_loaded = load_dotenv()
if not is_env_file_loaded: 
    raise FileNotFoundError(".env file was not found! or not exist is a root directory")

def test_demo_03(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    txt = RandomParagraphGenerator().generate_sentence()
    demo_qa_page.text_box_activity(current_address=txt, parmenant_address=txt)

def test_demo_04(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    downloads_path = DownloadsPathFinder().get_downloads_path()
    demo_qa_page.download_and_upload(path=downloads_path, file_name=TestData.FILE_NAME)
    time.sleep(5)
    os.remove(downloads_path+"\\"+TestData.FILE_NAME)

