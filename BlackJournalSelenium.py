from selenium import webdriver
from selenium.webdriver.common.by import By

# link to website
website = 'https://fixitplus.americanarchive.org/transcripts/cpb-aacip_62-7d2q52fm1v'

# chrome driver
options = webdriver.ChromeOptions()
# needed so website doesn't immediately close
options.add_experimental_option("detach", True)

# retrieves website using driver
driver = webdriver.Chrome(options=options)
driver.get(website)

# selenium iterates through given parameters for info
search_page = driver.find_elements(By.TAG_NAME, 'input')

for transcript in search_page:
    print(transcript.get_attribute('value'))



