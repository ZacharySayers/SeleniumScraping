from selenium import webdriver
from selenium.webdriver.common.by import By

# link to website
website = 'https://fixitplus.americanarchive.org/transcripts/cpb-aacip_62-7d2q52fm1v'

# path not needed anymore due to selenium update
# path = r"C:\Users\zsaye\Downloads\chromedriver_win32\chromedriver.exe")

# needed so website doesn't immediately close
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(website)

search_page = driver.find_elements(By.TAG_NAME, 'input')

for transcript in search_page:
    print(transcript.get_attribute('value'))


# the only input to give back some values

'''
transcript = driver.find_elements(By.TAG_NAME, "input")

#for phrases in transcript:
    #print(phrases)
'''


