from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo
import time
import numpy as np
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
    

def scrape():
    
    # Run splinter executable
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables for later reference.

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page in splinter browser
    browser.visit(url)

    time.sleep(5)    

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "lxml")

    # Retrieve the parent divs for all headlines and preview text
    results = soup.find_all("div", class_="list_text")

    # Create empty lists to append with headlines and preview text data
    headers = list()
    preview_texts = list()

    # loop over results to get headlines and preview text data
    for result in results:
        # scrape the article header 
        header = result.find("div", class_="content_title").text
        
        # scrape the article subheader
        preview_text = result.find("div", class_="article_teaser_body").text
        
        # print article data
        print('-----------------')
        print(header)
        print(preview_text)

        # Append lists with headlines and preview texts
        headers.append(header)
        preview_texts.append(preview_text)

    # URL of JPL page to be scraped
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

    # Retrieve page in splinter browser
    browser.visit(jpl_url)
    
    time.sleep(5)    

    # HTML object
    jpl_html = browser.html

    # Retrieve the parent divs for all articles
    jpl_soup = BeautifulSoup(jpl_html, 'lxml')

    # Retrieve featured image relative URL 
    featured_image = jpl_soup.find("img", class_="headerimage")["src"]

    # Clean up the webpage URL to combine with 
    # featured image relative URL to create full URL
    clean_url = jpl_url.split("index.html")

    # Concatenate URLs to create full featured image URL
    featured_image_url = clean_url[0] + featured_image

    print(featured_image_url)

    # URL of Space Facts page to be scraped
    facts_url = "https://space-facts.com/mars/"
    
    # Get all tables in URL via pandas
    tables = pd.read_html(facts_url)

    # Save relevant table as DataFrame and export to html
    df = tables[0]
    df = df.rename(columns={0:"Description",1:"Mars"})
    mars_table = df.to_html(index=False)

    # URL of Mars Hemispheres to be scraped
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Retrieve page in splinter browser
    browser.visit(hemi_url)

    # HTML object
    hemi_html = browser.html
    hemi_soup = BeautifulSoup(hemi_html, 'lxml')

    # Retrieve the parent divs for all articles
    hemi_results = hemi_soup.find_all("div", class_="item")

    # Retrieve all hemisphere links as a list
    hemispheres = list()

    for r in hemi_results:
        hemisphere = r.find("h3").text
        hemi_split = hemisphere.split(" Enhanced")
        hemi_clean = hemi_split[0]
        hemispheres.append(hemi_clean)
        
    hemisphere_image_urls = list()

    for hemi in hemispheres:
        try:
            # click on links with partial match "Enhanced"
            time.sleep(2)

            browser.click_link_by_partial_text(f"{hemi}")
            
            # get full image webpage URL and save as BeautifulSoup
            hemi_image_html = browser.html
            image_soup = BeautifulSoup(hemi_image_html, 'lxml')
            
            # find full image name and URL
            title = image_soup.find("h2", class_="title").text
            img_url = image_soup.find("div", class_="downloads").find("a")["href"]

            # remove word "Enhanced" from hemisphere name
            title_split = title.split(" Enhanced")
            title_clean = title_split[0]

            # print to check the code works
            print(title_clean)
            print(img_url)
            
            # append list with dictionary
            hemisphere_image_urls.append({"title":title_clean, "img_url":img_url})
            
            time.sleep(2)

            # click back
            browser.back()
            

        # stop code if all images scraped    
        except ElementDoesNotExist:
            print("Scraping Complete")

    # Store data in a dictionary
    mars_data = {
        "headers": headers,
        "preview_texts": preview_texts,
        "featured_image_url": featured_image_url, 
        "mars_table": mars_table,
        "hemispheres": hemispheres,
        "hemisphere_image_urls": hemisphere_image_urls,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data