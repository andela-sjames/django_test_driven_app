from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000/')
body = browser.find_element_by_tag_name('body')

assert 'Django' in body.text
browser.quit()