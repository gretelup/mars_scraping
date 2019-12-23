# Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs

def init_browser():
    """Initializes a splinter Browser object"""
    
    return Browser("chrome", executable_path="chromedriver", headless=True)

def news_scraper():

    """Scrapes the NASA Mars News Site and collect the latest news title and paragraph text.
    Returns a dictionary with the news title and paragraph text as strings."""
    
    # Open NASA Mars News Site using Splinter
    with init_browser() as browser:
        
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)

        # Create Beautiful soup object
        soup = bs(browser.html, "html.parser")

        # Get Latest News Title
        news_title= soup.find("div", class_="content_title").text.replace("\n", "")

        # Get Text for latest news 
        news_p = soup.find("div", class_= "rollover_description_inner").text
        
    # Create dictionary of results to return
    news_dict = {"news_title": news_title, "news_p": news_p}

    return(news_dict)

def image_scraper():
      
    """Scrapes the NASA Mars News Site and collects the image url for the current Featured Mars Image.
    Returns a dictionary with the news url as a string."""
    
    # Open NASA Mars News Site using Splinter
    with init_browser() as browser:
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)

        # Create Beautiful soup object
        soup = bs(browser.html, "html.parser")

        # Get image url for current Featured Mars Image
        JPL_image = soup.find("a", class_ = "button fancybox")["data-fancybox-href"]
        featured_image_url = f"https://www.jpl.nasa.gov{JPL_image}"

    # Create dictionary of results to return
    image_dict = {"featured_image_url": featured_image_url}
    return(image_dict)

def weather_scraper():
      
    """Scrapes the weather information from the most recent Mars weather Tweet.
    Returns a dictionary with the weather as a string"""
    
    # Open NASA Mars News Site using Splinter
    with init_browser() as browser:
        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)

        # Create Beautiful soup object
        soup = bs(browser.html, "html.parser")

        # Pull out text from tweet and format
        tweet_text = soup.find("div", class_="js-tweet-text-container").find("p").text
        mars_weather = " ".join(tweet_text.split("pic")[0].split("InSight ")[1].split("\n"))
    
    # Create dictionary of results to return
    weather_dict = {"mars_weather": mars_weather}
    return(weather_dict)

def facts_scraper():
      
    """Scrapes Facts about Mars from space-facts.com.
    Returns a dictionary with a string of html for a table of these facts"""
    
    # Convert table of facts from url into pandas dataframe
    url = "https://space-facts.com/mars/"
    facts_df = pd.read_html(url)[0]
    
    # Reformat dataframe
    facts_df = facts_df.rename(columns={1: "Value"})
    facts_df = facts_df.set_index(0)

    # Convert dataframe to htlp and clean up newlines
    html_facts = facts_df.to_html().replace("\n", "").replace('<tr style="text-align: right;">', '').\
    replace("    </tr>    <tr>      <th>0</th>      <th></th>    </tr>  ", "")
        
    # Create dictionary of results to return
    facts_dict = {"html_facts": html_facts}
    return(facts_dict)

def hemi_scraper():
      
    """Scrapes the name and url of high resolution images for each hemisphere of Mars.
    Returns a dictionary with a list of dictionaries of the image title and url for each hemisphere"""
    
    # Create list of hemisphere name and urls for each hemisphere in dictionary form
    hemisphere_image_urls = []
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    
    for x in range(4):
        with init_browser() as browser:
            
            browser.visit(url)

            # Create Beautiful soup object
            soup = bs(browser.html, "html.parser")
            
            hemi = soup.find_all("div", class_="description")[x]
            
            # Get name of hemisphere
            hemi_name = hemi.find("h3").text
            
            # Get link to page with full resolution image
            hemi_image = hemi.find("a")["href"]
            hemi_image_url = f"https://astrogeology.usgs.gov/{hemi_image}"
            
            with init_browser() as browser:
                # Open browser to selected hemisphere's page
                browser.visit(hemi_image_url)
                soup = bs(browser.html, "html.parser")

                # Get link to full resolution image
                hemi_full = soup.find("img", class_ = "wide-image")["src"]
                hemi_full_url = f"https://astrogeology.usgs.gov/{hemi_full}"
                
            hemi_image_dict = {"title": hemi_name, "img_url": hemi_full_url}      
            hemisphere_image_urls.append(hemi_image_dict)
    
    # Create dictionary of results to return
    hemi_dict = {"hemisphere_image_urls": hemisphere_image_urls}
    return(hemi_dict)

def scrape():
      
    """Scrapes various websites for information on Mars.
    Returns a dictionary of this information."""
    
    news_dict = news_scraper()
    image_dict = image_scraper()
    weather_dict = weather_scraper()
    facts_dict = facts_scraper()
    hemi_dict = hemi_scraper()

    mars_dict = {**news_dict, **image_dict, **weather_dict, **facts_dict, **hemi_dict}
    return(mars_dict)
