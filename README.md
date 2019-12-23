# Mars Scraping

Web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

![mission_to_mars](Images/mission_to_mars.png)

## Table of contents

* [About the Project](#about-the-project)
  * [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Development Process](#development-process)
* [Resources](#resources)
* [Contact](#contact)

## About the Project

words

## Technologies Used

* Python
  * beautifulsoup4 - version 4.8.1
  * Flask - version 1.1.1
  * numpy - version 1.17.4
  * pandas - version 0.25.3
  * pymongo - version 3.9.0
  * selenium - version 3.141.0
  * splinter - version 0.13.0
* HTML
* CSS
  * Bootstrap - version 4.1.3

## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites

* Chrome Web Browser
* Chromedriver
* MongoDB
  * [Mac Install Guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
  * [Windows Install Guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

### Installation

1. Clone the repo ```git clone https://github.com/gretelup/mars_scraping.git```

2. In a python 3 environment, `pip install requirements.txt`.

3. Run mongod to open a local connection.

4. Run `app.py` to host the page locally.

5. When accessing the page, click on the "Scrape" button to scrape the most recent data on the Mission to Mars and display it.

## Development Process

### Step 1 - Scraping

* Within a jupyter notebook, I scraped various websites for information and images on the Mission to Mars using BeautifulSoup, Pandas, and Splinter, entering the scraped data into a dictionary.

### Step 2 - MongoDB and Flask Application

* Then I converted the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data.
* Then I created a python Flask application with Jinja templating. Within the applications, I created the following routes:
    * A route called `/scrape` that will call the `scrape` function and store the return value in Mongo as a Python dictionary.
    * A root route `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.
* Finally, I created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

## Resources

* [NASA Mars News Site](https://mars.nasa.gov/news/)
* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
* [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en)
* [Mars Facts webpage](https://space-facts.com/mars/)
* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
