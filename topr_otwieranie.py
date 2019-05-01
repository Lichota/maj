from selenium import webdriver
browser = webdriver.Chrome('/Users/alichota/Downloads/chromedriver')
browser.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
browser.quit()