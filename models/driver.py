from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Driver:
    driver = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(executable_path=r"../chromedriver.exe", options=options)
        driver.get('https://pluginongkoskirim.com/cek-resi/')

        self.driver = driver

    def fetch_data(self, kurir, resi):
        if kurir == "Shopee Xpress":
            # TODO
            return

        kurir_input = Select(self.driver.find_element_by_name('kurir'))
        resi_input = self.driver.find_element_by_name('resi')
        search_button = self.driver.find_elements_by_class_name("form-submit")

        kurir_input.select_by_visible_text(kurir)

        resi_input.clear()
        resi_input.send_keys(resi)

        search_button[0].click()

        # Web loading
        try:
            while self.driver.find_element_by_class_name('form-loading'):
                continue
        except:
            None

        # If web can't find the awb, raise exception. Indicated by hasil[0] is out of range
        try: 
            hasil = self.driver.find_elements_by_class_name('cekresi-box')
            if hasil != None:
                return hasil[0].text
            else:
                print("Booo, datanya belom diload sama webnya. Mengulang query...")
                self.fetch_data(kurir, resi)
                return
        except:
            raise Exception("Nomor resi pada kurir tidak dapat ditemukan")

    def dispose(self):
        self.driver.quit()