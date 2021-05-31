from notion import Notion
from gcalender import GCalendar
import time

def main():
    ntn = Notion()
    ntn = ntn.getDatabaseContent()
    return ntn

results = main()
tmp = []
while True:
    tmp = main()
    if len(tmp) < len(results):
        results=tmp
        continue
    if not len(tmp) == len(results):
        gtn = GCalendar
        results = gtn.addEvent(tmp, results)
    time.sleep(10)