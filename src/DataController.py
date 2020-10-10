from selenium import webdriver
from selenium.webdriver import ActionChains
import time, os

class DataController(object):
    def __init__(self):
        self.url = "https://hk.investing.com/etfs/spdr-s-p-500-historical-data"
        self.driver = self.getDriver()
        self.email = "s88037zz@gmail.com"
        self.passwd = 's88037zz'

    def login(self):
        self.driver.get(self.url)

        elem_login = self.driver.find_element_by_xpath("//*[@class='login bold']")
        elem_login.click()
        time.sleep(1)

        # find the elements
        elem_email = self.driver.find_element_by_xpath("//*[@id='loginFormUser_email']")
        elem_passwd = self.driver.find_element_by_xpath("//*[@id='loginForm_password']")
        for elem in self.driver.find_elements_by_xpath("//a[@class='newButton orange']"):
            if elem.text == '登入':
                elem_login_btn = elem

        # set user info and click login button
        elem_email.send_keys(self.email)
        elem_passwd.send_keys(self.passwd)
        self.driver.execute_script("arguments[0].click()", elem_login_btn)
        time.sleep(2)

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def getDriver(self):
        options = self.getChromeOptions()
        driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
        return driver

    def getChromeOptions(self):
        download_dir = os.path.join(os.path.abspath(os.path.pardir), "data")
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': download_dir,
                 'directory_upgrade': True}
        options.add_experimental_option('prefs', prefs)
        return options

    def downlowSP500(self, start_date, end_date):
        self.driver.get(self.url)
        time.sleep(2)

        # change date range we download
        elem_date_range = self.driver.find_element_by_xpath("//*[@id='widgetFieldDateRange']")
        date_range = " - ".join((start_date, end_date))
        self.driver.execute_script("arguments[0].innerText = {}".format(date_range), elem_date_range)

        # download data
        elem_download = self.driver.find_element_by_xpath("//*[@title='下載數據']")
        elem_download.click()
        print("Download successfully")


if __name__ == '__main__':
    dc = DataController()
    dc.login()
    dc.downlowSP500('2020/01/01', '2020/10/09')