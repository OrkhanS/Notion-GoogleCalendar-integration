from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import datetime
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

class GCalendar:
    def addEvent(eventList, resultList):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)
        
        for n in eventList:
            if n in resultList or not "Due" in n['properties']:
                eventList.remove(n)
                continue
            event = {
                'summary': n['properties']['Name']['title'][0]['plain_text'],
                'start': {
                    'date': n['properties']['Due']['date']['start'],
                    'timeZone': 'Asia/Baku',
                },
                'end': {
                    'date': n['properties']['Due']['date']['start'],
                    'timeZone': 'Asia/Baku',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'popup', 'minutes': 2 * 60},
                    ],
                },
            }
            event = service.events().insert(calendarId='orkhan7887@gmail.com', body=event).execute()
            print ('Event created: %s' % (event.get('htmlLink')))

            resultList.append(event)
        return resultList
# if __name__ == '__main__':
#     main()