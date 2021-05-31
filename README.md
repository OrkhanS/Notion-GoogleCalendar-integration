# Notion and Google Calendar-integration


It is a simple Python script for Notion & Google Calendar integration.

## Installation

Clone the code, create a .env file with NOTION_SECRET, DATABASE_ID, and create credentials.json from Google Console API.

```bash
py main.py
```

## How It Works

The script periodically fetches the tasks list from the Notion Database and checks if it has been added to Google Calendar. Based on the "Name", "Due", "Created" properties of the list, it automatically adds the event to Google Calendar.                                                                        
(Property names can be customized)



![Test Image 3](https://github.com/OrkhanS/Notion-GoogleCalendar-integration/raw/main/notion_properties.png)


## License
[MIT](https://choosealicense.com/licenses/mit/)