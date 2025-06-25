#pip install requests ics

import requests
from ics import Calendar, Event
from datetime import datetime, timedelta
import subprocess

# === Settings ===
API_KEY = ''  # Replace with your Finnhub API key, registration needed
tickers = [''] # List out your interested stocks
ics_path = ""
applescript_path = ""

# === Biweekly Check (only even-numbered ISO weeks) ===
week_number = datetime.now().isocalendar()[1]
if week_number % 2 != 0:
    print("Skipping this week (off week)")
    exit()

# === Get Earnings in Next 30 Days ===
today = datetime.today()
future = today + timedelta(days=30)

url = f'https://finnhub.io/api/v1/calendar/earnings?from={today.date()}&to={future.date()}&token={API_KEY}'
response = requests.get(url)
data = response.json()

calendar = Calendar()
matched = 0

if 'earningsCalendar' in data:
    for entry in data['earningsCalendar']:
        symbol = entry.get('symbol')
        if symbol in tickers:
            date_str = entry['date']
            time_of_day = entry.get('hour', 'TBD')

            event = Event()
            event.name = f"{symbol} Earnings Report"
            event.begin = f"{date_str}T09:00:00"
            event.description = f"{symbol} earnings call ({time_of_day})"
            event.make_all_day()

            calendar.events.add(event)
            matched += 1

# === Save .ics File ===
with open(ics_path, 'w') as f:
    f.writelines(calendar)
print(f"ICS file generated with {matched} events.")

# === Auto-open ICS with Calendar ===
if matched > 0:
    subprocess.run(["osascript", applescript_path])
