# Extra links and resources used
# https://stackoverflow.com/questions/53025207/how-do-i-remove-name-and-dtype-from-pandas-output
# https://nfpdiscussions.udacity.com/t/build-gradually-test-frequently-scripting-for-the-bikeshare-project-step-by-step/213359

import time
import pandas as pd

CITY_DATA = {'C': 'chicago.csv',
             'N': 'new_york_city.csv',
             'W': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Getting user input for city (C = chicago, N = new york city, W = washington).
    city = input("To view bikeshare data please enter a city:\n'C' for Chicago, OR\n'N' for New York, OR\n'W' for Washington:\n").upper()
    # Validating user input
    while city not in CITY_DATA:
        print("That\'s not a valid city name")
        # Repeating the question again when input is not valid
        city = input("To view bikeshare data please enter a city:\n'C' for Chicago, OR\n'N' for New York, OR\n'W' for Washington:\n").upper()

    # conversions dictionary to convert months and all to usable month name
    months_conv = {"january": "january",
                   "february": "february",
                   "march": "march",
                   "april": "april",
                   "may": "may",
                   "june": "june",
                   "jan": "january",
                   "feb": "february",
                   "mar": "march",
                   "apr": "april",
                   "jun": "june",
                   "": "all",
                   "none": "all",
                   "all": "all"}
    # Getting user input for month (all, january, february, ... , june)
    month = input("Enter month to filter by month, (all, none or Enter to not filter by month):\n").lower()
    # Validating user input
    while month not in months_conv:
        print("That\'s not a valid input")

        month = input("Enter month to filter by month, (all, none or Enter to not filter by month):\n").lower()
    # Converting month input to usable month name (or all)
    month = months_conv[month]

    # conversions dictionary to convert days and all to usable day name
    days_conv = {"monday": "monday",
                 "tuesday": "tuesday",
                 "wednesday": "wednesday",
                 "thursday": "thursday",
                 "friday": "friday",
                 "sat": "saturday",
                 "sunday": "sunday",
                 "mon": "monday",
                 "tue": "tuesday",
                 "wed": "wednesday",
                 "thu": "thursday",
                 "fri": "friday",
                 "sat": "saturday",
                 "sun": "sunday",
                 "": "all",
                 "none": "all",
                 "all": "all"}
    # Getting user input for for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day to filter by day, (all, none or Enter for all days):\n").lower()
    # Validating user input
    while day not in days_conv:
        print("That\'s not a valid input")

        day = input("Enter day to filter by day, (all, none or Enter for all days):\n").lower()
    # Converting day input to usable day name (or all)
    day = days_conv[day]
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading specified city csv data into pandas data frame
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])  # Converting Start Time column to date-time
    df["Month"] = df["Start Time"].dt.month  # Adding Month column
    df["Day of Week"] = df["Start Time"].dt.day_name()  # Adding Day Name columns [df["Day of Week"] = df["Start Time"].dt.weekday_name()]

    # Filtering by Month if applicable
    if month != "all":  # if month doesn't equal "all"
        months = ["january", "february", "march", "april", "may", "june"]  # months list
        df = df.loc[df["Month"] == months.index(month) + 1]  # filtering by month number (+1 as list index starts with 0)

    # Filtering by day if applicable
    if day != "all":  # if day doesn't equal "all"
        df = df.loc[df["Day of Week"] == day.title()]  # filtering by day

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displaying the most common month
    months = ["", "january", "february", "march", "april", "may", "june"]  # List of months
    common_month = months[df["Month"].mode()[0]]  # Getting and converting the most common month number to month
    print("The most common month for the filtered data frame: ", common_month.title())  # Printing the most common month

    # Displaying the most common day of week
    print("The most common day of week for the filtered data frame: ", df["Day of Week"].mode()[0])

    # Displaying the most common start hour
    print("The most common hour for the filtered data frame", df["Start Time"].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displaying most commonly used start station
    print("The most commonly used start station for the filtered data frame: ", df["Start Station"].mode()[0])

    # Displaying most commonly used end station
    print("The most commonly used end station for the filtered data frame: ", df["End Station"].mode()[0])

    # Displaying most frequent combination of start station and end station trip
    common_trip = (df["Start Station"] + " | " + df["End Station"]).mode()[0]  # Finding most common trip by combining start and end stations
    print("The most commonly used trip for the filtered data frame: ", common_trip)  # Displaying common trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displaying total travel time
    print("Total travel time for the filtered data frame: ", df["Trip Duration"].sum())

    # Displaying mean travel time
    print("Mean travel time for the filtered data frame: ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types
    print("The count of each user type for the filtered data frame:\n", df["User Type"].value_counts().to_string())

    # Displaying counts of gender

    if city != "W":  # Checking as Washington data doesn't have gender nor birth year
        print("The count of gender for the filtered data frame:\n", df["Gender"].value_counts().to_string())  # Displaying counts of gender
        print("The earliest year of birth for the filtered data frame: ", df["Birth Year"].min())  # Displaying the earliest birth year
        print("The most recent year of birth for the filtered data frame: ", df["Birth Year"].max())  # Displaying the most recent birth year
        print("The most common year of birth for the filtered data frame: ", df["Birth Year"].mode()[0])  # Displaying the most common birth year

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def dsp_raw_data(df):
    """ Asking user if he wants to display sample of raw data """

    # Getting user input if he would like to list sample raw data
    raw_data_in = input("\nWould you like to see raw data sample? Enter yes or no:\n").lower()
    start_row = 0  # Row tracking initialization
    # Validating user input
    while raw_data_in == "yes" or raw_data_in == "y":  # While user inputs "yes" or "y"
        print(df.iloc[start_row:start_row + 5])  # Displaying 5 data rows starting from row tracking value
        start_row += 5  # Incrementing row tracking variable by 5
        raw_data_in = input("\nWould you like to see raw data sample? Enter yes or no:\n").lower()  # Re-questioning the user


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        dsp_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
