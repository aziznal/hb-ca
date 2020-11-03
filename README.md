# Hepsiburada - Comment Collector and Analyzer

### Project Description
This project consists of two parts:
1. Data Collection
2. Data Analysis


### The First Part - Data Collection
The first part will be done in python, using my own _[basic-web-scraper](https://github.com/aziznal/basic-web-scraper)_ package, and will consist of collecting comments from products in a few different categories.

The steps for data collection will be as follows:
1. Collect all product data from the thumbnails in each category. (25 to 50 pages == 400 to 1200 thumbnails per category)
2. Using data from step 1, visit each product URL and collect the full comment section data
3. Cleanup and save data from step 2 for analysis

To make filtering the data easier, I've created 3 data structures:
- __Thumbnail__: These are the components displayed in the 3 * 8 grid. they include an image of the product, as well as its price and rating, and most importantly, the product URL
- __Product__: This is used for the actual product page itself. It includes most relevant information about a product, but especially its comments in this case.
- __Comment__: This is used when dealing with each individual comment. It includes the author, the rating, and ofcourse, the comment body.

These datastructures are used as containers and are essential to simplify the scraping process.

The data collected is saved as a csv, and can be easily loaded using a library like pandas.

Using the script in its current state, any amount of pages for any category of products can be completely scraped for thumbnails.

_Note that the data saving script is a bit broken when dealing with quotes. To fix this I open each .csv file with excel and overwrite it. Excel takes care of the correct formating for me._


### The Second Part - Data Analysis
The Data Analysis part will be about applying some NLP techniques to use the collected data in a simple rating-prediction application.
