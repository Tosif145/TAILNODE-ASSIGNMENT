from requests_html import HTMLSession
import pymongo


# Python Intern Assignment PART-B
class BookScrap:
    def __init__(self):
        self.url = 'http://books.toscrape.com'

    # Function to scrape books data from a given URL
    def scrape_books_data(self, url):
        session = HTMLSession()
        response = session.get(url)
        books = []

        # Extracting book data from the page
        for book in response.html.find('article.product_pod'):
            title = book.find('h3 a', first=True).attrs['title']
            price = book.find('p.price_color', first=True).text
            availability = book.find('p.availability', first=True).text.strip()
            rating = book.find('p.star-rating', first=True).attrs['class'][1]
            books.append({'title': title, 'price': price, 'availability': availability, 'rating': rating})

        return books

    # Function to store scraped data in MongoDB database
    def store_data_in_database(self, data):
        print("Database Connection established....")
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["books_db"]
        collection = db["books"]
        collection.insert_many(data)
        client.close()

    # scraping the book to extract required fields
    def scrapBook(self):
        base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
        all_books = []

        for page_number in range(1, 51):
            url = base_url.format(page_number)
            books_data = self.scrape_books_data(url)
            all_books.extend(books_data)

        self.store_data_in_database(all_books)
        print('Data scraped and stored in database successfully!')


# Create an instance of the BookScrap class and run the scraping process
def runner():
    book_scraper = BookScrap()
    print("Fetching data wait for a while....")
    book_scraper.scrapBook()


runner()
