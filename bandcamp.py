import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = False

browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

tracks = browser.find_elements_by_class_name('discover-item')
len(tracks)
# tracks[4].click()

next_button = [e for e in browser.find_elements_by_class_name('item-page') if e.text.lower().find('next') > -1]
next_button[0].click()

time.sleep(1)

discover_section = browser.find_elements_by_class_name('discover-results')
left_x = discover_section[0].location['x']
right_x = left_x + discover_section[0].size['width']
discover_items = browser.find_elements_by_class_name('discover-item')
tracks = [t for t in discover_items if t.location['x'] >= left_x and t.location['x'] < right_x]
assert len(tracks) == 8
