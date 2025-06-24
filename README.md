# 📆 Stock Earnings Calendar Automation

Automatically generate and import stock earnings report dates into Apple Calendar on macOS using a Python script and AppleScript.

## 🔧 Features

- Pulls upcoming earnings dates for selected stocks using the Finnhub API
- Generates a `.ics` file with calendar events
- Auto-imports the `.ics` into Apple Calendar under a custom "Stock Earnings" calendar
- Scheduled to run automatically every other Monday via `launchd`
- Includes support for a rolling 30-day forecast window

## 💻 Technologies Used

- Python 3
- `ics` Python library
- AppleScript for calendar import
- `launchd` (macOS-native scheduler)
- Finnhub API

## 🗂️ File Overview

| File | Description |
|------|-------------|
| `earnings_calendar.py` | Main automation script (fetches earnings data, creates `.ics`, and triggers import) |
| `import_earnings_ics.scpt` | AppleScript that opens the calendar file to trigger import |

## ⚙️ How It Works

1. Script runs every 2 weeks using `launchd`
2. Fetches earnings reports for the next 30 days
3. Filters for a custom list of stock tickers
4. Generates calendar events in `.ics` format
5. Opens the file using AppleScript to trigger Calendar import

## 📌 Ticker List

Customizable list of tracked stock tickers:

## 📅 Calendar Setup

1. Manually create a new calendar in Apple Calendar called **"Stock Earnings"**
2. Set its color to green
3. Events will automatically be imported into this calendar

## 🕒 Scheduling

Set up using `launchd` on macOS to run:
- Every **Monday at 8:00 AM**
- Script includes logic to **only run every other week**

✨ Possible Enhancements
- Add reminders/alerts to calendar events
- Include estimated and actual EPS data
- Push .ics to Google Calendar
- Weekly email summaries
- Visual dashboard of upcoming earnings


