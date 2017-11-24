from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
import time;




driver = webdriver.Chrome();
driver.get("http://wbsec.gov.in/(S(o11dyg555mfwcn450q0abwu4))/DetailedResult/Detailed_gp.aspx");
districtSelect = Select(driver.find_element_by_name('ddldistrict'));
districtOption = districtSelect.options;
for districtValue in range(1,len(districtOption)):
	districtSelect.select_by_index(districtValue);

	panchayatSelect = Select(driver.find_element_by_name('ddlblock'));
	panchayatOption = panchayatSelect.options;
	for panchayatValue in range(1,len(panchayatOption)):
		panchayatSelect.select_by_index(panchayatValue);

		gpSelect = Select(driver.find_element_by_name('ddlgp'));
		gpOption = gpSelect.options;
		for gpValue in range(1,len(gpOption)):
			
			gpSelect = Select(driver.find_element_by_name('ddlgp'));
			gpSelect.select_by_index(gpValue);
			driver.implicitly_wait(10);
        	

        



			


		panchayatSelect = Select(driver.find_element_by_name('ddlblock'));

	districtSelect = Select(driver.find_element_by_name('ddldistrict'));

	


