from datetime import datetime, timedelta

def next_date(ndays):
    return datetime.now() + timedelta(days=ndays)

def _display(date, ndays):
    print("Date {} days form now : {}".format(ndays, date.strftime("%Y-%m-%d")))

if __name__ == "__main__":
    ndays = 1337
    date = next_date(ndays)
    _display(date, ndays)