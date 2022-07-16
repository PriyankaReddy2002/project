from selenium import webdriver
topic =input("Enter topic")
topic=topic.replace(' ','+')
browser =webdriver.Chrome('chromedriver')
for i in range(1):
    ele=browser.get("https://www.google.com/search?q="+topic+"&start"+str(i))
