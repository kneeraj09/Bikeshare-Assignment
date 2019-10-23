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
    cities = ['washington', 'new york city', 'chicago']
    city = input('Please enter one of the three cities you would like to explore: washington, new york city or chicago:').lower()
    while city not in cities:
        print('Please enter a valid city')
        city = input('Please enter one of the three cities you would like to explore: washington, new york city or chicago:').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    Month_or_Day = input('Would you like to analyse the data by month or day or both?').lower()
    if Month_or_Day == 'month':
        month = input('Please enter a month between January and June or all:').lower()
        day = 'all'
        return city, month, day
    elif Month_or_Day == 'day': 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        month = 'all'
        day = input ('Please enter a day of the week or all:').lower()
        return city, month, day
    elif Month_or_Day == 'both':
        month = input('Please enter a month between January and June or all:').lower()
        day = input ('Please enter a day of the week or all:').lower()
        return city, month, day   
    print('-'*40)
    
#print (get_filters())

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
    
    return df
# city, month, day = get_filters()
# print(load_data(city, month, day).head(5))      

def time_stats(df):
    print('Displays statistics on the most frequent times of travel.')

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['month'] = df['Start Time'].dt.month
    
    # TO DO: display the most common month
    months  = ['january', 'february', 'march', 'april', 'may', 'june']
    Most_Common_Month = df['month'].mode()[0] - 1
    Most_Common_Month = months[Most_Common_Month] 
    
    # TO DO: display thMost_Common_Month e most common day of week
    Most_Common_Day_of_Week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_Common_Start_Hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print ("Most Common day is: {}".format(Most_Common_Day_of_Week))
    print ("Most Common Month is: {}".format(Most_Common_Month))
    print ("Most Common Start Hour is: {}".format(Most_Common_Start_Hour))

#city, month, day = get_filters()
#df = pd.read_csv(CITY_DATA[city])
#time_stats(df)

def station_stats(df):
    print('Displays statistics on the most popular stations and trip.')

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
  
    # TO DO: display most commonly used start station
    Most_Common_Start_Station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    Most_Common_End_Station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station'] + '--to--'+ df ['End Station']
    Most_Common_Start_End = df['Start_End_Station'].mode()[0]
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print ("Most Common Start Station is: {}".format(Most_Common_Start_Station))
    print ("Most Common End Station is: {}".format(Most_Common_End_Station))
    print ("Most Common Start to End Station is: {}".format(Most_Common_Start_End))

#station_stats(df)


def trip_duration_stats(df):
    print ('\nDisplays statistics on the total and average trip duration.')
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total Travel Time in seconds was: {}'.format(Total_Travel_Time))

    # TO DO: display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean()
    print('Average Travel Time in seconds was: {}'.format(Average_Travel_Time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#trip_duration_stats(df)

def user_stats(df):
    print('Displays statistics on bikeshare users.')

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].dropna(axis=0)
        count_of_gender = gender.value_counts()
        print(count_of_gender)
    else:
        print ('City does not have Gender Data')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        YOB= df['Birth Year'].dropna(axis=0)
        Earliest_YOB = YOB.min()
        Most_Recent_YOB = YOB.max()
        Most_Common_YOB = YOB.mode()[0]
        
        print ('\nThe oldest person has a year of birth: {}'.format(Earliest_YOB))
        print ('The youngest person has a year of birth: {}'.format(Most_Recent_YOB))
        print('The most common year of birth: {}'.format(Most_Common_YOB))
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('Year of Birth information not available for city')   
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('Here is the firt 5 lines of data from your selection:')
        print (df.head())
        Head_Data = input('Do you want to see more data, please enter Yes or No ?').lower()
        i=0
        while Head_Data == 'yes':
            i += 5
            print (df.iloc[i:i+5])
            Head_Data = input('Do you want to see more data, please enter Yes or No ?').lower()
            if Head_Data == 'no':
                print(Head_Data)
                break;
     
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()