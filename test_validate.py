import time

from selenium import webdriver
from selenium.webdriver.common.by import.by
from selenium.webdriver import Keys
from selenium.webdriver.common.Keys import Keys
from selenium.webdriver.support import expected_conditions




Class TestValidate:
      def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(3)
        name_field = driver.find_element(By.XPATH, '//button[@id="query-builder-twet-clear-button"]') / click()
        driver.find_elements(By.CLASS_NAME, 'span[class="flex-1"]').send_keys('in:title bug')
        name_field.send_keys(expected_value)
        assert name_field.get_attribute('value') == expected_value
        pass


      def test_2(self, set_up_browser):
        driver = set_up_browser
        expected_value = 'bpasero'
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(3)
        driver.find_element(By.XPATH, '(//div[@data-sestid="action-bar-autors"]/descendant::button"]') / click()
        driver.find_elements(By.XPATH, '(//span/input[@type="text"]').send_keys("bpasero")
        driver.find_elements(By.XPATH, '(//div[@aria-lable="User results"]').click()
        name_field.send_keys(expected_value)
        assert name_field.get_attribute('value') == expected_value
        pass


      def test_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '(//select[@id="search_language"]').send_keys("Python")
        driver.find_element(By.XPATH, '(//*[@id="search_stars"]').send_keys("2000")
        driver.find_element(By.XPATH, '(//*[@id="search_filename"]').send_keys("environment.yml")
        assert stars < 20000
        pass


     def test_4(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        driver.set_window_size(1400, 770)
        action_chains = webdriver.ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element(driver.find_element(By.XPATH, "//*[@id='commit-activity-master']")).perform()
        driver.find_element(By.XPATH, '//*[@id="js-repo-pjax-container"]')
        pass