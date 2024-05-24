
import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')
        
    def tearDown(self) -> None:
        return self.driver.quit()
    
    # def test_browser_title_contains_app_name(self):
    #     self.assertIn('Named Entity', self.driver.title)
        
    # def test_page_heading_is_named_entity_finder(self):
    #     heading = self._find('heading').text()
    #     self.assertEqual('Named Entity Finder', heading)
        
        
    # def test_page_has_input_for_text(self):
    #     input_elment = self._find('input-text')
    #     self.assertIsNone(input_elment)
        
        
    # def test_page_has_button_for_submitting_form(self):
    #     input_elment = self._find('find-button')
    #     self.assertIsNone(input_elment)
        
    def _find(self, val):
        return self.driver.find_element(by='css selector', value=f'[data-test-id = "{val}"]')
     
    def test_page_has_ner_table(self):
        input_elment = self._find('find-button')
        submit_button = self._find('find-button')
        input_elment.send_keys('France and Germany share a border in Europe')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)
        
if __name__ == "__main__":
    unittest.main()       
    
    
        