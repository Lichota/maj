# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
#
# def test_example(driver):
#     driver.get('http://www.onet.pl/')
#     driver.find_element_by_name('q').send_keys("webdriver")
#     driver.find_element_by_name('btnG').click()
#     WebDriverWait(driver, 10).until(EC.title_is('webdriver - wyszukiwanie Google'))



from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/alichota/Downloads/chromedriver')
driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
title = driver.title
print(title)
assert 'Demobank - Bankowość Internetowa - Logowanie' == title
driver.quit()




