import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta
import json

load_dotenv()
  
class Notion:
    NOTION_SECRET = os.getenv('NOTION_SECRET')
    DATABASE_ID = os.getenv('DATABASE_ID')

    def getDatabaseContent(self):
        today = date.today()
        yesterday = today - timedelta(days = 1)

        url = "https://api.notion.com/v1/databases/" + self.DATABASE_ID + '/query'
        query = {"filter": {"property": "Created", "date": { "on_or_after": yesterday.isoformat()}}, "sorts": [{"timestamp": "created_time", "direction": "descending"}]}
        

        headers = {
            'Authorization': 'Bearer ' + self.NOTION_SECRET,
            'Notion-Version': '2021-05-13'
        }
        data = requests.post(url, headers=headers, json=query).json()
        return data['results']