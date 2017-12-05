from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.common.exceptions import NoSuchElementException
import time;


data_list = []

driver = webdriver.Firefox()
driver.get("http://www.wbsec.gov.in/(S(tqjmgl55rl2vw1bnrtih2r45))/DetailedResult/Detailed_gp_2013.aspx")


# first loop for district

districtSelect = Select(driver.find_element_by_name('ddldistrict'))
districtOption = districtSelect.options



for districtValue in range(5,len(districtOption)):
	districtSelect = Select(driver.find_element_by_name('ddldistrict'))
	
	districtSelect.select_by_index(districtValue)

	# second loop for panchayat

	panchayatSelect = Select(driver.find_element_by_name('ddlblock'))
	panchayatOption = panchayatSelect.options;

	for panchayatValue in range(1,len(panchayatOption)):

		panchayatSelect = Select(driver.find_element_by_name('ddlblock'))

		panchayatSelect.select_by_index(panchayatValue);

		# third loop for gram ponchayet 

		gpSelect = Select(driver.find_element_by_name('ddlgp'))
		gpOption = gpSelect.options

		for gpValue in range(1,len(gpOption)):
			try:
				gpSelect = Select(driver.find_element_by_name('ddlgp'))
				gpSelect.select_by_index(gpValue)

				print_button = WebDriverWait(driver, 30).until(
	    			EC.presence_of_element_located((By.XPATH, '//input[@id = "btnprint"]'))
				)
				print_button.click()
				districtSelect = Select(driver.find_element_by_name('ddldistrict'))
				districtOption = districtSelect.options
				panchayatSelect = Select(driver.find_element_by_name('ddlblock'))
				panchayatOption = panchayatSelect.options;
				gpSelect = Select(driver.find_element_by_name('ddlgp'))
				gpOption = gpSelect.options
				with open("test.txt", "a") as myfile:
					myfile.write(districtOption[districtValue].text + ' ' + panchayatOption[panchayatValue].text + ' ' + gpOption[gpValue].text + '\n')

				time.sleep(5)
			except NoSuchElementException:
				driver.save_screenshot("filename2.png")
				driver.back()
				
			
			
