#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo
import time
import numpy as np
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# # Step 1 - Scraping
# <hr>

# ### NASA Mars News Site
# <p> Scrape NASA Mars news site for latest headlines and preview text

# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables for later reference.

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page in splinter browser
browser.visit(url)


# In[4]:


# HTML object
html = browser.html

# Retrieve the parent divs for all articles
soup = BeautifulSoup(html, 'lxml')


# #### Minor gotcha: website needs to be run through Splinter before scraping with BeautifulSoup, otherwise it won't appear in BeautifulSoup's scrape

# In[5]:


# Retrieve the parent divs for all headlines and preview text
results = soup.find_all("div", class_="list_text")


# In[7]:


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


# ### NASA JPL Images
# <p> Scrape NASA Mars news site for latest headlines and preview text

# In[8]:


# URL of JPL page to be scraped
jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

# Retrieve page in splinter browser
browser.visit(jpl_url)


# In[9]:


# HTML object
jpl_html = browser.html

# Retrieve the parent divs for all articles
jpl_soup = BeautifulSoup(jpl_html, 'lxml')


# In[10]:


# Retrieve featured image relative URL 
featured_image = jpl_soup.find("img", class_="headerimage")["src"]


# #### Minor gotcha: JPL url needs to have the "index.html" suffix removed before appending the image's relative URL

# In[11]:


# Clean up the webpage URL to combine with 
# featured image relative URL to create full URL
clean_url = jpl_url.split("index.html")


# In[12]:


# Concatenate URLs to create full featured image URL
featured_image_url = clean_url[0] + featured_image


# In[13]:


featured_image_url


# ### Mars Facts
# <p> Scrape Space Facts website for space facts

# In[14]:


# URL of Space Facts page to be scraped
facts_url = "https://space-facts.com/mars/"


# In[15]:


# Get all tables in URL via pandas
tables = pd.read_html(facts_url)
tables


# In[16]:


# Save relevant table as DataFrame
df = tables[0]


# In[17]:


# Rename column headers to appropriate names
df = df.rename(columns={0:"Description",1:"Mars"})


# In[18]:


# Export table as HTML string, remove superfluous index
df.to_html('table.html', index=False)


# ### Mars Hemispheres
# <p> Scrape USGS Astrogeology website for Mars hemispheres facts

# In[19]:


hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# Retrieve page in splinter browser
browser.visit(hemi_url)


# 
# hemisphere_image_urls = list()
# 
# for image in images:
#     click on links with partial match "Enhanced"
#     title = soup.find("h2", class_="title").text
#     img_url = soup.find("div", class_="downloads").find("a")[i]["href"]
#     
#     title_strip = title.strip(" ")
#     title_clean = f"{title_strip[0]} {title_strip[1]}"
#     
#     hemisphere_image_urls.append({"title":title_clean, "img_url":img_url})
#     click back
#     
# 

# In[20]:


# HTML object
hemi_html = browser.html

# Retrieve the parent divs for all articles
hemi_soup = BeautifulSoup(hemi_html, 'lxml')


# In[21]:


hemi_results = hemi_soup.find_all("div", class_="item")


# In[28]:


hemispheres = list()

for r in hemi_results:
    hemisphere = r.find("h3").text
    hemi_split = hemisphere.split(" ")
    hemispheres.append(hemi_split[0])
    
hemispheres


# In[38]:


hemisphere_image_urls = list()

for hemi in hemispheres:
    try:
        # click on links with partial match "Enhanced"
        browser.click_link_by_partial_text(f"{hemi}")
        
        # get full image webpage URL and save as BeautifulSoup
        hemi_image_html = browser.html
        image_soup = BeautifulSoup(hemi_image_html, 'lxml')
        
        # find full image name and URL
        title = image_soup.find("h2", class_="title").text
        img_url = image_soup.find("div", class_="downloads").find("a")["href"]

        # remove word "Enhanced" from hemisphere name
        title_split = title.split(" ")
        title_clean = f"{title_split[0]} {title_split[1]}"

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


# In[39]:


hemisphere_image_urls


# # Step 2 - MongoDB and Flask Application
# <hr>

# In[ ]:




