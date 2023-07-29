import csv
import sys
from pathlib import Path
from datetime import datetime, date, timedelta

TODAY_PATH = Path("files")
TODAY_PATH.mkdir(parents=True, exist_ok=True)

##############################################################################
# Below functionality sets or retrieves global argument TODAY


if not Path("files/today.csv").is_file():  # create a 'today file' if not exist
    TODAY = date.today()
    with open("files/today.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["todays_date", TODAY])

else:  # open today.csv to retrieve the date that has been stored as 'today'
    with open("files/today.csv", "r") as file:
        reader = csv.reader(file)
        TODAY = datetime.strptime(next(reader)[1], "%Y-%m-%d").date()


#############################################################################
# Date manipulation functions:


def set_date(date_obj):
    with open("files/today.csv", "w+") as file:
        writer = csv.writer(file)
        writer.writerow(["todays_date", date_obj])


def change_date(today, no_of_days):
    today += timedelta(days=(int(no_of_days)))
    set_date(today)
    return today


##############################################################################
# Functions that validate whether the CL arguments are in correct date format:


def valid_date(date_str):
    """validates whether the input date has format 'YYYY-MM-DD'
    or converts 'today' or 'yesterday' strings to a valid date.
    returns date object"""

    if date_str == "today":
        date_obj = TODAY
        print("Today's date is set to ", TODAY)
        return date_obj
    elif date_str == "yesterday":
        date_obj = TODAY - timedelta(days=1)
        print("Yesterday's date is set to ", date_obj)
        return date_obj
    else:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print(
                f"'{date_str}' not a valid_date.",
                "Please enter a date in format 'YYYY-MM-DD'",
            )
            sys.exit()


def valid_month(date_str):
    """validates whether the input date has format 'YYYY-MM',
    returns date object"""

    try:
        return datetime.strptime(date_str, "%Y-%m").date()
    except ValueError:
        print(
            f"'{date_str}' not a valid month.",
            "Please enter a date in format 'YYYY-MM'",
        )
        sys.exit()


def valid_year(date_str):
    """validates whether the input date has format 'YYYY-MM',
    returns date object"""

    try:
        return datetime.strptime(date_str, "%Y").date()
    except ValueError:
        print(
            f"'{date_str}' not a valid year.",
            "Please enter a date in format 'YYYY'",
        )
        sys.exit()
