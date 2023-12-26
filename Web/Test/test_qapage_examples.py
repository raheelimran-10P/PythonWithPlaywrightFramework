import logging
from dotenv import load_dotenv
from Web.Pages.demo_qa_page import DemoQaPage
from Web.TestData.test_data import TestData
from Web.Util.DownloadsPathFinder import DownloadsPathFinder
from Web.Util.random_paragraph_util import RandomParagraphGenerator
from allure import step, attach
from playwright.sync_api import expect
import os
import time
import allure


# Load environment variables from the .env file ay the root of the project
# used any sensitive information like PASSWORD=os.getenv("PASSWORD")
is_env_file_loaded = load_dotenv()
if not is_env_file_loaded: 
    raise FileNotFoundError(".env file was not found! or not exist is a root directory")

@allure.title("Test Box Activity")
@allure.description("This test is add text in text fileds.\n\nNote that this test is a demo test.")
@allure.tag("NewUI", "Essentials")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("qa", TestData.QA_PERSON)
@allure.link(TestData.URL, name="Website")
@allure.testcase("", name="DV-0000")
def test_demo_01(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    title = demo_qa_page.page.title()
    assert title == 'DEMOQA', f"Unexpected title: {title}"
    txt = RandomParagraphGenerator().generate_sentence()
    demo_qa_page.text_box_activity(current_address=txt, parmenant_address=txt)
    expect(page.get_by_text("Name:default")).to_be_visible()

@allure.title("Download and Upload Activity")
@allure.description("This test is to download file and upload that file.\n\nNote that this test is a demo test.")
@allure.tag("NewUI", "Essentials")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("qa", TestData.QA_PERSON)
@allure.link(TestData.URL, name="Website")
@allure.testcase("", name="DV-0000")
def test_demo_02(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    title = demo_qa_page.page.title()
    assert title == 'DEMOQA', f"Unexpected title: {title}"
    downloads_path = DownloadsPathFinder().get_downloads_path()
    demo_qa_page.download_and_upload(path=downloads_path, file_name=TestData.FILE_NAME)
    expect(page.get_by_text("sampleFile.jpeg")).to_be_visible()
    time.sleep(5)
    os.remove(downloads_path+"\\"+TestData.FILE_NAME)

@allure.title("Practice Form Activity")
@allure.description("This test is to perform activity on practise form.\n\nNote that this test is a demo test.")
@allure.tag("NewUI", "Essentials")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("qa", TestData.QA_PERSON)
@allure.link(TestData.URL, name="Website")
@allure.testcase("", name="DV-0000")
def test_demo_03(set_up_tear_down) -> None:
    page = set_up_tear_down
    demo_qa_page = DemoQaPage(page)
    logging.info("Starting the test...")
    demo_qa_page.nagivate_to(TestData.URL)
    title = demo_qa_page.page.title()
    assert title == 'DEMOQA', f"Unexpected title: {title}"
    demo_qa_page.practice_form()