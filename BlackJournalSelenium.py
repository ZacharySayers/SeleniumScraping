from selenium import webdriver
from selenium.webdriver.common.by import By

website = 'https://fixitplus.americanarchive.org/transcripts/cpb-aacip_62-7d2q52fm1v'

# path not needed anymore due to selenium update
# path = r"C:\Users\zsaye\Downloads\chromedriver_win32\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(website)

search_page = driver.find_elements(By.XPATH, './/*[@id="transcript-lines"]/div')

for transcript in search_page:
    print(transcript.getAttribute("value"))

# the only input to give back some values
'''
transcript = driver.find_elements(By.TAG_NAME, "input")

#for phrases in transcript:
    #print(phrases)
'''


