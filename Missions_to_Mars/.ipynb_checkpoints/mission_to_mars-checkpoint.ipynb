{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd\n",
    "import pymongo\n",
    "import time\n",
    "import numpy as np\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1 - Scraping\n",
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### NASA Mars News Site\n",
    "<p> Scrape NASA Mars news site for latest headlines and preview text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 88.0.4324\n",
      "[WDM] - Get LATEST driver version for 88.0.4324\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [C:\\Users\\WelanR_01\\.wdm\\drivers\\chromedriver\\win32\\88.0.4324.96\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. \n",
    "# Assign the text to variables for later reference.\n",
    "\n",
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "\n",
    "# Retrieve page in splinter browser\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML object\n",
    "html = browser.html\n",
    "\n",
    "# Retrieve the parent divs for all articles\n",
    "soup = BeautifulSoup(html, 'lxml')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Minor gotcha: website needs to be run through Splinter before scraping with BeautifulSoup, otherwise it won't appear in BeautifulSoup's scrape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve the parent divs for all headlines and preview text\n",
    "results = soup.find_all(\"div\", class_=\"list_text\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----------------\n",
      "Testing Proves Its Worth With Successful Mars Parachute Deployment\n",
      "The giant canopy that helped land Perseverance on Mars was tested here on Earth at NASA’s Wallops Flight Facility in Virginia.\n",
      "-----------------\n",
      "NASA's Perseverance Rover Gives High-Definition Panoramic View of Landing Site\n",
      "A 360-degree panorama taken by the rover’s Mastcam-Z instrument will be discussed during a public video chat this Thursday.\n",
      "-----------------\n",
      "Nearly 11 Million Names of Earthlings are on Mars Perseverance\n",
      "When the Perseverance rover safely touched down on the Martian surface, inside Jezero Crater, on Feb. 18, 2021, it was also a safe landing for the nearly 11 million names on board.\n",
      "-----------------\n",
      "NASA's Mars Perseverance Rover Provides Front-Row Seat to Landing, First Audio Recording of Red Planet \n",
      "The agency’s newest rover captured first-of-its kind footage of its Feb. 18 touchdown and has recorded audio of Martian wind.\n",
      "\n",
      "\n",
      "-----------------\n",
      "NASA to Reveal New Video, Images From Mars Perseverance Rover\n",
      "First-of-its kind footage from the agency’s newest rover will be presented during a briefing this morning.\n",
      "-----------------\n",
      "NASA's Mars Helicopter Reports In \n",
      "The technology demonstration has phoned home from where it is attached to the belly of NASA’s Perseverance rover. \n",
      "-----------------\n",
      "NASA's Perseverance Rover Sends Sneak Peek of Mars Landing\n",
      "The six-wheeled robot’s latest data since touching down yesterday include a hi-res image captured as the rover’s jetpack lowered it to the ground.\n",
      "-----------------\n",
      "Touchdown! NASA's Mars Perseverance Rover Safely Lands on Red Planet\n",
      "The agency’s latest and most complex mission to the Red Planet has touched down at Jezero Crater. Now it’s time to begin testing the health of the rover.  \n",
      "-----------------\n",
      "Searching for Life in NASA's Perseverance Mars Samples\n",
      "When the agency’s newest rover mission searches for fossilized microscopic life on the Red Planet, how will scientists know whether they’ve found it?\n",
      "-----------------\n",
      "The Mars Relay Network Connects Us to NASA's Martian Explorers\n",
      "A tightly choreographed dance between NASA’s Deep Space Network and Mars orbiters will keep the agency’s Perseverance in touch with Earth during landing and beyond.\n",
      "-----------------\n",
      "NASA's Next Mars Rover Is Ready for the Most Precise Landing Yet\n",
      "What to expect when the Mars 2020 Perseverance rover arrives at the Red Planet on Feb. 18, 2021.\n",
      "-----------------\n",
      "Sensors Prepare to Collect Data as Perseverance Enters Mars' Atmosphere\n",
      "Technology will collect critical data about the harsh entry environment during Perseverance’s entry next Thursday.\n",
      "-----------------\n",
      "InSight Is Meeting the Challenge of Winter on Dusty Mars\n",
      "As dust collects on the solar panels and winter comes to Elysium Planitia, the team is following a plan to reduce science operations in order to keep the lander safe.\n",
      "-----------------\n",
      "NASA Invites Public to Share Thrill of Mars Perseverance Rover Landing\n",
      "Mark your calendars for live landing commentary, news briefings, livestreamed Q&As, virtual watch parties, student activities, and more.\n",
      "-----------------\n",
      "Tricky Terrain: Helping to Assure a Safe Rover Landing\n",
      "How two new technologies will help Perseverance, NASA’s most sophisticated rover yet, touch down onto the surface of Mars this month.\n",
      "-----------------\n",
      "Where Should Future Astronauts Land on Mars? Follow the Water\n",
      "A new NASA paper provides the most detailed map to date of near-surface water ice on the Red Planet.\n",
      "-----------------\n",
      "NASA's Perseverance Pays Off Back Home\n",
      "Even as the Perseverance rover approaches Mars, technology on board is paying off on Earth.\n",
      "-----------------\n",
      "Could the Surface of Phobos Reveal Secrets of the Martian Past?\n",
      "The Martian moon Phobos orbits through a stream of charged atoms and molecules that flow off the Red Planet’s atmosphere, new research shows.\n",
      "-----------------\n",
      "NASA's MAVEN Continues to Advance Mars Science and Telecommunications Relay Efforts\n",
      "With a suite of new national and international spacecraft primed to explore the Red Planet after their arrival next month, NASA’s MAVEN mission is ready to provide support and continue its study of the Martian atmosphere.\n",
      "-----------------\n",
      "NASA's Perseverance Rover 22 Days From Mars Landing\n",
      "Seven minutes of harrowing descent to the Red Planet is in the not-so-distant future for the agency’s Mars 2020 mission.  \n",
      "-----------------\n",
      "6 Things to Know About NASA's Mars Helicopter on Its Way to Mars\n",
      "Ingenuity, a technology experiment, is preparing to attempt the first powered, controlled flight on the Red Planet.\n",
      "-----------------\n",
      "NASA to Host Virtual Briefing on February Perseverance Mars Rover Landing\n",
      "NASA leadership and members of the mission will discuss the agency’s latest rover, which touches down on the Red Planet on Feb. 18.\n",
      "-----------------\n",
      "NASA InSight's ‘Mole' Ends Its Journey on Mars\n",
      "The heat probe hasn’t been able to gain the friction it needs to dig, but the mission has been granted an extension to carry on with its other science.\n",
      "-----------------\n",
      "Mars 2020 Perseverance Rover to Capture Sounds From the Red Planet\n",
      "Audio gathered by the mission may not sound quite the same on Mars as it would to our ears on Earth. A new interactive online experience lets you sample the difference.\n",
      "-----------------\n",
      "NASA's Curiosity Rover Reaches Its 3,000th Day on Mars\n",
      "As the rover has continued to ascend Mount Sharp, it’s found distinctive benchlike rock formations.\n",
      "-----------------\n",
      "Celebrate the Perseverance Rover Landing With NASA's Student Challenge\n",
      "The rover touches down on the Red Planet next month, and students are invited to join the excitement by designing, building, and landing their own Mars mission. NASA can help.\n",
      "-----------------\n",
      "NASA Extends Exploration for Two Planetary Science Missions\n",
      "The missions – Juno and InSight – have each increased our understanding of our solar system, as well as spurred new sets of diverse questions.\n",
      "-----------------\n",
      "7 Things to Know About the NASA Rover About to Land on Mars\n",
      "The Mars 2020 Perseverance rover, which has started its approach to the Red Planet, will help answer the next logical question in Mars exploration.\n",
      "-----------------\n",
      "A Martian Roundtrip: NASA's Perseverance Rover Sample Tubes\n",
      "Marvels of engineering, the rover's sample tubes must be tough enough to safely bring Red Planet samples on the long journey back to Earth in immaculate condition. \n",
      "-----------------\n",
      "NASA Moves Forward With Campaign to Return Mars Samples to Earth\n",
      "During this next phase, the program will mature critical technologies and make critical design decisions as well as assess industry partnerships.\n",
      "-----------------\n",
      "3 Things We've Learned From NASA's Mars InSight \n",
      "Scientists are finding new mysteries since the geophysics mission landed two years ago.\n",
      "-----------------\n",
      "From JPL's Mailroom to Mars and Beyond\n",
      "Bill Allen has thrived as the mechanical systems design lead for three Mars rover missions, but he got his start as a teenager sorting letters for the NASA center.\n",
      "-----------------\n",
      "5 Hidden Gems Are Riding Aboard NASA's Perseverance Rover\n",
      "The symbols, mottos, and small objects added to the agency's newest Mars rover serve a variety of purposes, from functional to decorative.\n",
      "-----------------\n",
      "MOXIE Could Help Future Rockets Launch Off Mars\n",
      "NASA's Perseverance rover carries a device to convert Martian air into oxygen that, if produced on a larger scale, could be used not just for breathing, but also for fuel.\n",
      "-----------------\n",
      "Hear Audio From NASA's Perseverance As It Travels Through Deep Space\n",
      "The first to be rigged with microphones, the agency's latest Mars rover picked up the subtle sounds of its own inner workings during interplanetary flight.\n",
      "-----------------\n",
      "Mars Is Getting a New Robotic Meteorologist\n",
      "Sensors on NASA's Perseverance will help prepare for future human exploration by taking weather measurements and studying dust particles.\n",
      "-----------------\n",
      "Heat and Dust Help Launch Martian Water Into Space, Scientists Find\n",
      "Scientists using an instrument aboard NASA’s Mars Atmosphere and Volatile EvolutioN, or MAVEN, spacecraft have discovered that water vapor near the surface of the Red Planet is lofted higher into the atmosphere than anyone expected was possible. \n",
      "-----------------\n",
      "NASA's Curiosity Takes Selfie With 'Mary Anning' on the Red Planet\n",
      "The Mars rover has drilled three samples of rock in this clay-enriched region since arriving in July.\n",
      "-----------------\n",
      "Independent Review Indicates NASA Prepared for Mars Sample Return Campaign\n",
      "NASA released an independent review report Tuesday indicating the agency is well positioned for its Mars Sample Return campaign to bring pristine samples from Mars to Earth for scientific study.\n",
      "-----------------\n",
      "NASA's Perseverance Rover 100 Days Out\n",
      "Mark your calendars: The agency's latest rover has only about 8,640,000 seconds to go before it touches down on the Red Planet, becoming history's next Mars car.\n"
     ]
    }
   ],
   "source": [
    "# Create empty lists to append with headlines and preview text data\n",
    "headers = list()\n",
    "preview_texts = list()\n",
    "\n",
    "# loop over results to get headlines and preview text data\n",
    "for result in results:\n",
    "    # scrape the article header \n",
    "    header = result.find(\"div\", class_=\"content_title\").text\n",
    "    \n",
    "    # scrape the article subheader\n",
    "    preview_text = result.find(\"div\", class_=\"article_teaser_body\").text\n",
    "    \n",
    "    # print article data\n",
    "    print('-----------------')\n",
    "    print(header)\n",
    "    print(preview_text)\n",
    "\n",
    "    # Append lists with headlines and preview texts\n",
    "    headers.append(header)\n",
    "    preview_texts.append(preview_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### NASA JPL Images\n",
    "<p> Scrape NASA Mars news site for latest headlines and preview text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of JPL page to be scraped\n",
    "jpl_url = \"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html\"\n",
    "\n",
    "# Retrieve page in splinter browser\n",
    "browser.visit(jpl_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML object\n",
    "jpl_html = browser.html\n",
    "\n",
    "# Retrieve the parent divs for all articles\n",
    "jpl_soup = BeautifulSoup(jpl_html, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve featured image relative URL \n",
    "featured_image = jpl_soup.find(\"img\", class_=\"headerimage\")[\"src\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Minor gotcha: JPL url needs to have the \"index.html\" suffix removed before appending the image's relative URL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Clean up the webpage URL to combine with \n",
    "# featured image relative URL to create full URL\n",
    "clean_url = jpl_url.split(\"index.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate URLs to create full featured image URL\n",
    "featured_image_url = clean_url[0] + featured_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts\n",
    "<p> Scrape Space Facts website for space facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of Space Facts page to be scraped\n",
    "facts_url = \"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get all tables in URL via pandas\n",
    "tables = pd.read_html(facts_url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save relevant table as DataFrame\n",
    "df = tables[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename column headers to appropriate names\n",
    "df = df.rename(columns={0:\"Description\",1:\"Mars\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export table as HTML string, remove superfluous index\n",
    "df.to_html('table.html', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Hemispheres\n",
    "<p> Scrape USGS Astrogeology website for Mars hemispheres facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemi_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "# Retrieve page in splinter browser\n",
    "browser.visit(hemi_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "hemisphere_image_urls = list()\n",
    "\n",
    "for image in images:\n",
    "    click on links with partial match \"Enhanced\"\n",
    "    title = soup.find(\"h2\", class_=\"title\").text\n",
    "    img_url = soup.find(\"div\", class_=\"downloads\").find(\"a\")[i][\"href\"]\n",
    "    \n",
    "    title_strip = title.strip(\" \")\n",
    "    title_clean = f\"{title_strip[0]} {title_strip[1]}\"\n",
    "    \n",
    "    hemisphere_image_urls.append({\"title\":title_clean, \"img_url\":img_url})\n",
    "    click back\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML object\n",
    "hemi_html = browser.html\n",
    "\n",
    "# Retrieve the parent divs for all articles\n",
    "hemi_soup = BeautifulSoup(hemi_html, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemi_results = hemi_soup.find_all(\"div\", class_=\"item\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus', 'Schiaparelli', 'Syrtis', 'Valles']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemispheres = list()\n",
    "\n",
    "for r in hemi_results:\n",
    "    hemisphere = r.find(\"h3\").text\n",
    "    hemi_split = hemisphere.split(\" \")\n",
    "    hemispheres.append(hemi_split[0])\n",
    "    \n",
    "hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n",
      "Schiaparelli Hemisphere\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n",
      "Syrtis Major\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n",
      "Valles Marineris\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "hemisphere_image_urls = list()\n",
    "\n",
    "for hemi in hemispheres:\n",
    "    try:\n",
    "        # click on links with partial match \"Enhanced\"\n",
    "        browser.click_link_by_partial_text(f\"{hemi}\")\n",
    "        \n",
    "        # get full image webpage URL and save as BeautifulSoup\n",
    "        hemi_image_html = browser.html\n",
    "        image_soup = BeautifulSoup(hemi_image_html, 'lxml')\n",
    "        \n",
    "        # find full image name and URL\n",
    "        title = image_soup.find(\"h2\", class_=\"title\").text\n",
    "        img_url = image_soup.find(\"div\", class_=\"downloads\").find(\"a\")[\"href\"]\n",
    "\n",
    "        # remove word \"Enhanced\" from hemisphere name\n",
    "        title_split = title.split(\" \")\n",
    "        title_clean = f\"{title_split[0]} {title_split[1]}\"\n",
    "\n",
    "        # print to check the code works\n",
    "        print(title_clean)\n",
    "        print(img_url)\n",
    "        \n",
    "        # append list with dictionary\n",
    "        hemisphere_image_urls.append({\"title\":title_clean, \"img_url\":img_url})\n",
    "        \n",
    "        time.sleep(2)\n",
    "        \n",
    "        # click back\n",
    "        browser.back()\n",
    "        \n",
    "    # stop code if all images scraped    \n",
    "    except ElementDoesNotExist:\n",
    "        print(\"Scraping Complete\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2 - MongoDB and Flask Application\n",
    "<hr>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
