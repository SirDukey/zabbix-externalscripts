#!/usr/local/bin/python3.7
from selenium import webdriver

url = 'http://print.novusgroup.co.za/view.php'
browser = webdriver.PhantomJS()
browser.get(url)
browser.set_window_size(1024, 768)
page_ocr = browser.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]')
article_ocr = browser.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[2]')
'''
print('Page:', page_ocr.text)
print('Article:', article_ocr.text)
'''
page = page_ocr.text
art = article_ocr.text
page_file = open('OCR_page_stats.txt', 'w')
art_file = open('OCR_art_stats.txt', 'w')
page_file.write(str(page_ocr.text))
art_file.write(str(article_ocr.text))
page_file.close()
art_file.close()

browser.quit()
