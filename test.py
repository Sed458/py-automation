import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True

# assert opts.headless # Operating in headless mode

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

time.sleep(1)

results = browser.find_elements_by_class_name('result')
print(results[0].text)

browser.close()
quit()