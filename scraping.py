import time
from selenium import webdriver
import os

def scraping(query='python'):
    path = os.getcwd() + '/chromedriver'

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path,options=options)
    try:
        driver.get('https://qiita.com/tags/' + query + '?page=1')

        trend_tag = driver.find_element_by_class_name('p-tagShow_mainMiddle')
        trends = trend_tag.find_elements_by_class_name('tst-ArticleBody_title')
        trend_texts = []
        trend_urls = []
        for trend in trends:
            trend_texts.append(trend.text)
            trend_urls.append(trend.get_attribute('href'))

        driver.quit()

        return trend_texts , trend_urls
    except:
        driver.quit()
        return [] , []

if __name__ == "__main__":
    trends = scraping()
    for i in range(5):
        text = trends[0][i] + '\n' + trends[1][i]
        print(text)