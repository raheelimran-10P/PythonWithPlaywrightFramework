from playwright.sync_api import expect, Page, Browser
from Web.TestData.test_data import TestData
import time

class DemoQaPage:

    def __init__(self, page: Page):
        self.page = page
        self._elements = page.get_by_text("Elements") 
        self._text_box = page.get_by_text("Text Box") 
        self._text_filed_name = page.get_by_placeholder("Full Name")
        self._text_filed_email = page.get_by_placeholder("name@example.com")
        self._text_filed_current_address = page.locator('#currentAddress')
        self._text_filed_parmenant_address = page.locator('#permanentAddress')
        self._button_submit = page.locator('#submit')
        self._upload_and_download = page.get_by_text("Upload and Download")
        self._button_download = page.locator('#downloadButton')
        self._select_file = page.locator('#uploadFile')

    def nagivate_to(self, url):
        self.page.goto(url)

    def text_box_activity(self, current_address, parmenant_address, name="default", email="name@example.com"):
        self._elements.click()
        expect(self._text_box).to_be_visible()  
        self._text_box.click()
        expect(self._text_filed_name).to_be_visible()  
        expect(self._text_filed_name).to_be_editable()
        self._text_filed_name.clear()
        self._text_filed_name.fill(name)
        expect(self._text_filed_email).to_be_visible()  
        expect(self._text_filed_email).to_be_editable()
        self._text_filed_email.clear()
        self._text_filed_email.fill(email)
        expect(self._text_filed_current_address).to_be_visible()  
        expect(self._text_filed_current_address).to_be_editable()
        self._text_filed_current_address.clear()
        self._text_filed_current_address.fill(current_address)
        expect(self._text_filed_parmenant_address).to_be_visible()  
        expect(self._text_filed_parmenant_address).to_be_editable()
        self._text_filed_parmenant_address.clear()
        self._text_filed_parmenant_address.fill(parmenant_address)
        expect(self._button_submit).to_be_visible() 
        self._button_submit.click() 

    def download_and_upload(self, path, file_name):
        self._elements.click()
        expect(self._upload_and_download).to_be_visible()  
        self._upload_and_download.click()
        expect(self._button_download).to_be_visible()  
        with self.page.expect_download() as download_info:
            self._button_download.click()
        download = download_info.value
        download.save_as(path+"\\"+ download.suggested_filename)
        expect(self._select_file).to_be_visible()  
        self._select_file.set_input_files(path+"\\"+file_name, timeout=TestData.TIMEOUT_IN_MILLISECONDS)        



        


    
