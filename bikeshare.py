import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    available_cities = list(CITY_DATA.keys())
    print('the data available for only these cities {}'.format(available_cities))
    city = 'not selected yet'
    while city not in available_cities :
          city = input('please enter a name of one of the above cities to get  its data: ').lower()
          if city not in available_cities :
             print("Sorry , we don't have the data of this city. You can choose one from this list{}".format(available_cities))
    # TO DO: get user input for month (all, january, february, ... , june)
    all_months = ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'september' , 'october' , 'november' , 'december']
    month = 'not selected yet'
    while month not in all_months and month != 'all':
          month = input('Please Enter a  valid Month name . If you want all months type "all". ').lower()
          if month not in all_months and month != 'all' :
            print('{} is not a valid name for a month, please type a valid one.'.format(month))
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    all_days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    day = 'not selected yet'
    while day not in all_days and day != 'all':
        day = input("please type a name of a day . If you want the data of all days type'all'. ").lower()
        if day not in all_days and day != 'all' :
            print('{} it is not a valid name for a day please try again. '.format(day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Gives the First 5 lines in filtered raw data if the user want that.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    all_months = ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'september' , 'october' , 'november' , 'december']
    
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all' :
        month = all_months.index(month) + 1
        df = df[df['month'] == month ]
    if day != 'all' :
        df = df[df['day'] == day.title()]
    print_raw_data = input(' Do you want to see the first 5 lines in your filtered raw data ? (y/n): ').lower()
    if print_raw_data  in ['y' , 'yes'] : 
        print(df.head())
        input('Type any letter to continue :  ')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format( df['month'].mode()[0]))
    # TO DO: display the most common day of week
    print('The  most  common day is: {}'.format(df['day'].mode()[0]))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The  most common hour is : {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start Station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common  end  station is : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    freq = df.groupby(['Start Station' , 'End Station']).size().nlargest(1).reset_index(name = 'No_of_times')
    #print(freq)
    print('The  most  common combination is  \n \n {}'.format(freq))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration = round(df['Trip Duration'].sum()/60/60 , 2)
    print('Total Travel Time       is {} Hour(s)'.format(duration))

    # TO DO: display mean travel time
    mean_duration = round(df['Trip Duration'].mean()/60/60 , 2)
    print('The Mean of travel time is {} Hour(s)'.format(mean_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('count of each user type:\n{}'.format(df.groupby(['User Type'])['User Type'].count()))


    # TO DO: Display counts of gender
    print('Count of each gender : \n{}'.format(df.groupby(['Gender'])['Gender'].count()))


    # TO DO: Display earliest, most recent, and most common year of birth
    print('The Earliest  year  of birth  is : {}'.format(int(df['Birth Year'].min())))
    print('The most recent year of birth is : {}'.format(int(df['Birth Year'].max())))
    print('The most common year of birth is : {}'.format(int(df['Birth Year'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
