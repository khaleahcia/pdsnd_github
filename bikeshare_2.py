import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}



def get_filters():
    """
    Ask user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
            month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
            day filter
    """
    print('H   H    EEEEE    L        L         OOOO     !!!')
    print('H   H    E        L        L        O    O    !!!')
    print('H   H    E        L        L        O    O    !!!')
    print('HHHHH    EEEEE    L        L        O    O    !!!')
    print('H   H    E        L        L        O    O    !!!')
    print('H   H    E        L        L        O    O')
    print('H   H    EEEEE    LLLLL    LLLLL     OOOO     !!!')
    print('\nLet\'s explore some US bikeshare data!')

    # Gets valid user input for city (chicago, new york city, washington).
    city = get_input(
        '\nDo you want to see data from Chicago, New York, or Washington? ', CITY_DATA)

    # Gets valid user input for month (all, january, february, ... , june)
    month = get_input('\nWhich month do you want to filter the data by?\nChoose January, February, March, April, May, June, or all. ', [
                      'all', 'january', 'february', 'march', 'april', 'may', 'june'])

    # Gets valid user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input('\nWhich day of the week do you want to fliter by?\nChoose Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all. ', [
                    'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

    print('-'*40)
    return city, month, day


def get_input(question, filter_info):
    """
    Get the input from user and checks to see if input is valid

    Args:
        (str) question - text of question asking user for correct input
        (sequence type) filter_info - list or dictionary that has valid inputs
            in lowercase

    Returns:
        (str) String of valid data in lowercase
    """
    while True:
        # Asks user for input
        value = input(question).lower()

        # Checks to see if input is valid
        if value in filter_info:
            print('\nYou picked {}.'.format(value.title()))
            return value
        else:
            print('\nInvalid input. Please try again.')


def load_data(city, month, day):
    """
    Load data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
            month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
            day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loads data file
    df = pd.read_csv(CITY_DATA[city])

    # Converts Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Creates month column from Start Time
    df['month'] = df['Start Time'].dt.month

    # Creates day of week column from Start Time
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filters by month if month is not all
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Filters by day of the week if day is not all
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most common month
    x = str(df['month'].mode())
    x = int(x[5:6])
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most frequent month of travel: ' + months[x-1])

    # Displays the most common day of week
    print('\nThe most frequent day of the week to travel: '
          + str(df['day_of_week'].mode()))

    # Sisplays the most common start hour
    start_hour = df['Start Time'].dt.hour
    print('\nThe most frequent start hour: ' + str(start_hour.mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displays most commonly used start station
    print('Most common start station: {}\n'.format(df['Start Station'].mode()))
    print(df['Start Station'].value_counts())

    # Displays most commonly used end station
    print('\nMost common end station: {}\n'.format_map(
        df['End Station'].mode()))
    print(df['End Station'].value_counts())

    # Displays most frequent combination of start station and end station trip
    print('\nMost common trip: '
          + str(df.groupby(['Start Station', 'End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays total travel time
    print('Total travel time: ' + str(df['Trip Duration'].sum()))

    # Displays mean travel time
    print('\nTravel time mean: ' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    print('User Types     Count\n' + '-'*25
          + '\n' + str(df['User Type'].value_counts()))

    if city == 'washington':
        print('\nGender data not available for Washington.')
        print('\nBirth year data not available for Washington.')
    else:
        # Displays counts of gender
        print('\nGender     Count\n' + '-'*25
              + '\n' + str(df['Gender'].value_counts()))

        # Displays earliest, most recent, and most common year of birth
        print('\nEarliest birth year: '
              + str(df['Birth Year'].min(skipna=True)))
        print('\nMost recent birth year: '
              + str(df['Birth Year'].max(skipna=True)))
        print('\nMost common birth year: ' + str(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
<<<<<<< HEAD
    """Display raw data from dataframe."""
    raw_data_question = input('\nWould you like to see raw data? Enter yes or no.\n')
=======
    """Displays raw data from dataframe"""
    raw_data_question = input(
        '\nWould you like to see raw data? Enter yes or no.\n')
>>>>>>> refactoring
    if raw_data_question.lower() != 'yes':
        return
    print('-'*40)
    index = df.index.min()
    while True:
        for x in range(5):
            print(df.iloc[index])
            print('\n')
            index += 1
        if index >= df.index.max():
            break
        raw_data_question = input('\nContinue? Enter yes or no.\n')
        if raw_data_question.lower() != 'yes':
            break
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
