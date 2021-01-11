from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time

class ScrapeMars():
    def __init__(self):
        pass

    def init_browser(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        return browser

    def scrape_info(self):
        # open dictionary to fill to put into MongoDB
        scraped_data = {}
        browser = self.init_browser()

        # NASA news scraping
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        time.sleep(1)

        data = BeautifulSoup(browser.html)
        slide = data.find("li", {"class": "slide"})
        news_title = slide.find("div", {"class": "content_title"}).text.strip()
        news_p = slide.find("div", {"class": "article_teaser_body"}).text.strip()

        # featured URL
        base = "https://www.jpl.nasa.gov"
        url = f"{base}/spaceimages/?search=&category=Mars"
        browser.visit(url)
        time.sleep(1)

        browser.find_by_id("full_image").click()
        time.sleep(1)

        browser.find_link_by_partial_text("more info").click()
        time.sleep(1)

        data = BeautifulSoup(browser.html)
        image = data.find("img", {"class": "main_image"})

        featured_image_url  = base + image["src"]

        # Mars facts scraping
        url = "https://space-facts.com/mars/"
        browser.visit(url)
        time.sleep(1)

        dfs = pd.read_html(browser.html)
        df = dfs[0]
        df.columns = ["Statistic", "Value"]
        mars_facts = df.to_html(index=False)

        # Hemisphere data scraping

        base = "https://astrogeology.usgs.gov"
        url = f"{base}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        time.sleep(1)

        data = BeautifulSoup(browser.html)
        links = data.find("div", {"class": "results"}).findAll("a", {"class": "itemLink"})

        #filter out non image results
        realLinks = []
        for link in links:
            image = link.find("img")
            if (image):
                realLinks.append(base + link["href"]) # append the base url

        # LOOP through each image link, click, grab the image info
        hemisphere_data = []
        for realLink in realLinks:
            browser.visit(realLink)
            time.sleep(1)

            data = BeautifulSoup(browser.html)
            hemi_url = data.find("ul").find("li").find("a")["href"]
            hemi_title = data.find("h2", {'class', "title"}).text.split(" Enhanced")[0]

            hemisphere_data.append({"title": hemi_title, "url": hemi_url})

        #exit browser
        browser.quit()

        #add data to dictionary for mongo
        scraped_data["news_title"] = news_title
        scraped_data["news_p"] = news_p
        scraped_data["featured_image_url"] = featured_image_url
        scraped_data["mars_facts"] = mars_facts
        scraped_data["hemispheres"] = hemisphere_data
        
        # results
        return scraped_data