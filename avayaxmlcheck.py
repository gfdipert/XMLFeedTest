import urllib2
from urllib2 import urlopen
from selenium import webdriver
import lxml
import xml.etree.ElementTree as etree

xml_file = urllib2.urlopen('https://www.avaya.com/Chat/avaya.com/RSSFeedProd-en_US.xml')
xml_data = xml_file.read()


zifturl = raw_input('Enter url here: ')
driver = webdriver.Chrome(executable_path='/Users/gwendipert/Documents/chromedriver')
driver.get(zifturl)

def format(word):
	word = word.text.encode('ascii','ignore')
	return word

#Zift Content Title
title = driver.find_element_by_xpath('//h1/span')
title = format(title)

#XML
print 'Check for Content Title'
print '<Content_Title>{0}</Content_Title>'.format(title) in xml_data

#Zift subtitle
subtitle = driver.find_element_by_xpath('//b/span/div')
subtitle = format(subtitle)

#XML
print 'Check for Subtitle'
print '{0}'.format(subtitle) in xml_data





