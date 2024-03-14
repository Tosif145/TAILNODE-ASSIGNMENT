import requests
import pymongo
import pandas


# Python Intern Assignment PART-A
class ApiConnection:
    def __init__(self):

        # Connecting to database and creating collection
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["TosifDB"]
        self.user_collection = self.db["userData"]
        self.posts_collection = self.db["postsData"]

        # api url and api key
        self.url = 'https://dummyapi.io/data/v1/user'
        self.api_key = '65f1d4eb2d8e5b385d53473c'
        self.header = {
            "Content-type": "application/json",
            "Accept-Encoding": "deflate",
            "app-id": self.api_key
        }

    # Fetching data
    def fetch_data(self):
        response = requests.get(self.url, headers=self.header)
        response_data = response.json()
        df = pandas.json_normalize(response_data, 'data')
        return df

    # Storing user information
    def store_user_data(self, df):
        # Convert dataframe to dictionary format
        data_dict = df.to_dict(orient='records')

        # Insert data into MongoDB
        self.user_collection.insert_many(data_dict)

        # Fetch Users List from Database
        users = self.user_collection.find()
        return users

    # Storing posts related to user
    def store_posts_data(self, users):
        for user in users:
            user_id = user['id']
            user_posts_url = f'https://dummyapi.io/data/v1/user/{user_id}/post'
            response = requests.get(user_posts_url, headers={"app-id": self.api_key})

            if response.status_code == 200:
                posts_data = response.json()['data']
                for post in posts_data:
                    # Insert posts data into MongoDB
                    self.posts_collection.insert_one(post)
            else:
                print(f"Failed to fetch posts data for user {user_id}")
        print('Data fetched and stored in database successfully!.')


def runner():
    api_connection = ApiConnection()
    print('connection successful...')
    user_data = api_connection.fetch_data()
    users = api_connection.store_user_data(user_data)
    api_connection.store_posts_data(users)


runner()
