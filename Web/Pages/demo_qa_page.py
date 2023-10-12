from playwright.sync_api import expect, Page, Browser

class DemoQaPage:

    def __init__(self, page: Page):
        self.page = page
        self._elements = page.get_by_text("Elements") 
        self._text_box = page.get_by_text("Text Box") 

    def nagivate_to(self, url):
        self.page.goto(url)

    def text_box_activity(self):
        self._elements.click()
        expect(self._text_box).to_be_visible()  
        self._text_box.click()

    

        


    
