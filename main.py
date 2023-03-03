from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")

browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver.exe')

browser.implicitly_wait(10)

browser.get('https://www.google.com/')

browser.find_element(By.NAME, 'q').send_keys('tempo agora São Paulo')

browser.find_element(By.NAME,'btnK').click()

temperature = browser.find_element(By.ID,'wob_tm').text

browser.quit()

print('A temperatura é ' + str(temperature))

txt = open('./teste.txt', 'a')
txt.write('Temperatura de ' + str(temperature) + '\n')
txt.close
