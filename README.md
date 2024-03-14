# API Data Fetch and Book Scrap Scripts

## Part A - API Data Fetch (`api_data_fetch.py`):

This script, `api_data_fetch.py`, is responsible for fetching user data and their corresponding posts from an external API (`https://dummyapi.io/data/v1/user`) and storing it in a MongoDB database.

### `ApiConnection` Class:
- Establishes a connection to the MongoDB database and initializes collections for storing user data and posts.
- Provides methods to fetch user data, store user information in the database, and store posts related to users.

### Execution:
To run the script, execute the `runner()` function within the script.

## Part B - Book Scrap (`books.py`):

This script, `books.py`, is used to scrape book data from a website (`http://books.toscrape.com`) and store it in a MongoDB database.

### `BookScrap` Class:
- Implements methods to scrape book data from the website and store it in a MongoDB database.
- Utilizes the `requests_html` library for web scraping.

### Execution:
To run the script, execute the `runner()` function within the script.

