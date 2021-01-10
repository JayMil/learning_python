import os
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

def main():
    readCsvDateFormat()


def readCsvDateFormat():
    plt.style.use('seaborn')

    exampledir = os.path.dirname(__file__)
    data = pd.read_csv(os.path.join(exampledir, 'data.csv'))

    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    price_date = data['Post Date']
    balance = data['Balance']

    plt.plot_date(price_date, balance, linestyle='solid')

    # fit date labels better
    plt.gcf().autofmt_xdate()

    plt.title("Account Balance")
    plt.xlabel("Date")
    plt.ylabel("Balance")

    plt.tight_layout()
    plt.show()

def basicDateFormat():
    plt.style.use('seaborn')

    dates = [
            datetime(2019, 5, 24),
            datetime(2019, 5, 25),
            datetime(2019, 5, 26),
            datetime(2019, 5, 27),
            datetime(2019, 5, 28),
            datetime(2019, 5, 29),
            datetime(2019, 5, 30)
    ]

    y = [0, 1, 3, 4, 6, 5, 7]

    plt.plot_date(dates, y, linestyle='solid')

    # fit date labels better
    plt.gcf().autofmt_xdate()

    # update date format to "Month, day year" - "Feb, 3 2010"
    date_format = mpl_dates.DateFormatter('%b, %d %Y')
    plt.gca().xaxis.set_major_formatter(date_format)

    #plt.title("Most Popular Languages")
    #plt.xlabel("Number of People Who Use")
    #plt.ylabel("Number of People Who Use")


    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
