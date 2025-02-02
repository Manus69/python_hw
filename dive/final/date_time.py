from datetime import datetime

def datetime_display():
    now = datetime.now()

    print("Current date and time: {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))
    print("Day of the week : {}".format(now.strftime("%A")))
    print("Week : {}".format(now.isocalendar()[1]))

if __name__ == "__main__":
    datetime_display()

