from playwright.sync_api import expect, Page, Browser
from Web.TestData.test_data import TestData
import time
import logging

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
        self._form = page.get_by_text("Forms")
        self._practice_form = page.get_by_text("Practice Form")
        self._first_name = page.locator('#firstName')
        self._last_name = page.locator('#lastName')
        self._user_email = page.locator('#userEmail')
        self._male = page.get_by_text("Male", exact=True)
        self._user_number = page.get_by_placeholder("Mobile Number")
        self._hobbie = page.get_by_text("Sports")
        self._book_store_link = page.get_by_text("Book Store Application")
        self._login = page.locator("xpath=//span[contains(text(),'Login')]")
        self._username = page.locator("xpath=//input[@id='userName']")
        self._password = page.locator("xpath=//input[@id='password']")
        self._login = page.get_by_role("button", name="Login")

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

    def practice_form(self, first_name="first name", 
                            last_name="last name", 
                            user_email="abc@gmail.com", 
                            user_number="03546265668",
                            subject="subject"
                        ):
        self._form.click()
        expect(self._practice_form).to_be_visible()  
        self._practice_form.click()
        expect(self._first_name).to_be_visible()  
        expect(self._first_name).to_be_editable()
        self._first_name.clear()
        self._first_name.fill(first_name)
        expect(self._last_name).to_be_visible()  
        expect(self._last_name).to_be_editable()
        self._last_name.clear()
        self._last_name.fill(last_name)
        expect(self._user_email).to_be_visible()  
        expect(self._user_email).to_be_editable()
        self._user_email.clear()
        self._user_email.fill(user_email)
        expect(self._male).to_be_visible()        
        if not self._male.is_checked():
            self._male.check()
        expect(self._user_number).to_be_visible()  
        expect(self._user_number).to_be_editable()
        self._user_number.clear()
        self._user_number.fill(user_number)
        if not self._hobbie.is_checked():
            self._hobbie.check()

    def login_activity(self, username: str, password: str) -> None:
        expect(self._book_store_link).to_be_visible()
        self._book_store_link.click()
        expect(self._login).to_be_visible()
        self._login.click()
        expect(self._username).to_be_editable()
        self._username.clear()
        self._username.fill(username)
        expect(self._password).to_be_editable()
        self._password.clear()
        self._password.fill(password)
        expect(self._login).to_be_enabled()
        self._login.click()
        expect(self.page.get_by_text(username)).to_be_visible()





        


    
