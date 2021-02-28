from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time

class CalculatorTest(unittest.TestCase):
    
    # This def used for driver set up
    def setUp(self):
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.calculator.net/")
    
    # This def used for addition operation
    def test_addition(self):
        self.all_operators_list=[]
        self.operators_list=[]
        self.all_numbers_list=[]
        self.driver.get("https://www.calculator.net/")
        add_number=["–234234","+","345345"]
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "sciop"]'):
            self.all_operators_list.append(elem)
            self.operators_list.append(elem.text)
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "scinm"]'):
            self.all_numbers_list.append(elem)
        for n in add_number:
            for i in n:
                if i in self.operators_list:
                    for j in self.all_operators_list:
                        if j.text==i:
                            j.click()
                else:
                    for j in self.all_numbers_list:
                        if j.text==i:
                            j.click()
        value = self.driver.find_element_by_id("sciOutPut")
        self.assertEqual(111111, int(value.text))
        print("Addition operation successfully done")
        time.sleep(3)
    
    # This def used for substraction operation
    def test_sub(self):
        self.all_operators_list=[]
        self.operators_list=[]
        self.all_numbers_list=[]
        self.driver.get("https://www.calculator.net/")
        sub_number=["234823","–","–23094823"]
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "sciop"]'):
            self.all_operators_list.append(elem)
            self.operators_list.append(elem.text)
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "scinm"]'):
            self.all_numbers_list.append(elem)
        for n in sub_number:
            for i in n:
                if i in self.operators_list:
                    for j in self.all_operators_list:
                        if j.text==i:
                            j.click()
                else:
                    for j in self.all_numbers_list:
                        if j.text==i:
                            j.click()
        value = self.driver.find_element_by_id("sciOutPut")
        self.assertEqual(23329646, int(value.text))
        print("Substraction operation successfully done")        
        time.sleep(3)

    # This def used for multipication operation
    def test_mul(self):
        self.all_operators_list=[]
        self.operators_list=[]
        self.all_numbers_list=[]
        self.driver.get("https://www.calculator.net/")
        mul_number=["423","×","525"]
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "sciop"]'):
            self.all_operators_list.append(elem)
            self.operators_list.append(elem.text)
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "scinm"]'):
            self.all_numbers_list.append(elem)
        for n in mul_number:
            for i in n:
                if i in self.operators_list:
                    for j in self.all_operators_list:
                        if j.text==i:
                            j.click()
                else:
                    for j in self.all_numbers_list:
                        if j.text==i:
                            j.click()
        value = self.driver.find_element_by_id("sciOutPut")
        self.assertEqual(222075, int(value.text))
        print("Multipication  operation successfully done")        
        time.sleep(3)

    # This def used for Division operation
    def test_div(self):
        self.all_operators_list=[]
        self.operators_list=[]
        self.all_numbers_list=[]
        self.driver.get("https://www.calculator.net/")
        div_number=["4000","/","200"]
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "sciop"]'):
            self.all_operators_list.append(elem)
            self.operators_list.append(elem.text)
        for elem in self.driver.find_elements_by_xpath('.//span[@class = "scinm"]'):
            self.all_numbers_list.append(elem)
        for n in div_number:
            for i in n:
                if i in self.operators_list:
                    for j in self.all_operators_list:
                        if j.text==i:
                            j.click()
                else:
                    for j in self.all_numbers_list:
                        if j.text==i:
                            j.click()
        value = self.driver.find_element_by_id("sciOutPut")
        self.assertEqual(20, int(value.text))
        print("Division operation successfully done")        
        time.sleep(3)

    # This def which is invoked last cleans the Selenium driver
    def tearDown(self):
            #close the browser window
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)


