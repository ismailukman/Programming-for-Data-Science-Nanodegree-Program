import pandas as pd
import numpy as np

#CLI Dashboard for US bikeshare states

city_record = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def load_data(city, month, day):
    db_cty = pd.read_csv(city_record[city])
    db_cty['Start Time'] = pd.to_datetime(db_cty['Start Time'])
    db_cty['Month'] = db_cty['Start Time'].dt.month
    db_cty['Day of Week'] = db_cty['Start Time'].dt.weekday_name
    db_cty['Hour'] = db_cty['Start Time'].dt.hour
    if month != 'a':
        month = months.index(month)+1
        db_cty = db_cty[db_cty['Month'] == month]
    if day != 'a':
        db_cty = db_cty[db_cty['Day of Week'] == day.title()]

    return db_cty

def select_data():
    #Choose a city
    print('Welcome to US City Bike Dashboard!')
    while True:
        city = input('Select City\n1=Chicago, 2=New York, or 3=Washington \n').lower()
        if(city=='1'):
            city = "chicago"
            break
        if(city=='2'):
            city = "new york"
            break
        if(city=='3'):
            city = "washington"
            break
        if city in city_record:
            break
        else: 
            print('Invalid entry of state. Please try again. \n')
            
    while True:
        month = input('Select Month?\n 1=January 2=February 3=March 4=April 5=May 6=June, or "a" to get all record. \n').lower()
        if(month=="1"):
            month = "january"
            break
        if(month=="2"):
            month = "february"
            break
        if(month=="3"):
            month = "march"
            break
        if(month=="4"):
            month = "april"
            break
        if(month=="5"):
            month = "may"
            break
        if(month=="6"):
            month = "june"
            break
        #city.lower()
        
        if month in months or month == 'a':
            break
        else:
            print('Invalid Month Selected. Please try again. \n')
            
    while True:
        day = input('Select Week?\n 1=Monday 2=Tuesday 3=Wednesday 4=Thursday 5=Friday 6=Saturday 7=Sunday or "a" to get all record. \n').lower()
        if(day=="1"):
            day = "monday"
            break
        if(day=="2"):
            day = "tuesday"
            break
        if(day=="3"):
            day = "wednesday"
            break
        if(day=="4"):
            day = "thursday"
            break
        if(day=="5"):
            day = "Friday"
            break
        if(day=="6"):
            day = "saturday"
            break
        if(day=="7"):
            day = "sunday"
            break 
        #day.lower()
        
        if day in days or day == 'a':
            break
        else:
            print('Invalid Week selected. Please try again. \n')
    print('*'*50)
    return city, month, day


def time_info(db_cty): 
    frequent_month = db_cty['Month'].mode()[0]
    frequent_day = db_cty['Day of Week'].mode()[0]
    frequent_hour = db_cty['Hour'].mode()[0]
    print("Summary of frequency")
    print('Monthly higest rentage is {}.\nWeekly higest rentage is {}.\nHourly highest rentage is {}.'.format(frequent_month, frequent_day, frequent_hour))
    print('*'*50)


def station_info(db_cty): 
    frq_start_st = db_cty['Start Station'].mode()[0]
    frq_end_st = db_cty['End Station'].mode()[0]
    db_cty['Start and End Stations'] = db_cty['Start Station'] + ' ===> ' + db_cty['End Station']
    freq_tr = db_cty['Start and End Stations'].mode()[0]

    print('Riders most prefered start station {}.\nRiders Most prefered stop station {}.\nMost Friquent Trip {}.'.format(frq_start_st, frq_end_st, freq_tr))
    print('*'*50)


def trip_info(db_cty): 
    total_time = db_cty['Trip Duration'].sum()
    mean_time = db_cty['Trip Duration'].mean()
    print('Total Trip hours is {}.\nAverage of each trip is {} minutes.'.format(round(total_time/3600, 2), round(mean_time/60, 2)))
    print('*'*50)


def bikers_info(db_cty): 
    user_type = db_cty['User Type'].value_counts()
    gender_count = 'no record from this city.'
    oldest_year = 'no record from this city'
    youngest_year = oldest_year
    bd_year = oldest_year
    if 'Gender' in db_cty:
        gender_count = db_cty['Gender'].value_counts()
    if 'Birth Year' in db_cty:
        oldest_year = int(db_cty['Birth Year'].min())
        youngest_year = int(db_cty['Birth Year'].max())
        bd_year = int(db_cty['Birth Year'].mode()[0])
    print('The gender distibution of riders\n{}\n\nThe oldest was born in {}.\nThe youngest was born in {}.\nHigest Birth year coincidence occur in {}.'.format(gender_count, oldest_year, youngest_year, bd_year))
    print('*'*50)

    
def view_more(city, db_cty):
    initial = 0
    added_row = 7
    while True:
        check = input('\nView additional 7 rows for {} ? Enter y=yes or n=no.'.format(city.title())).lower()
        if check == 'y':
            print(db_cty.iloc[initial:added_row])
            initial += 7
            added_row += 7
        elif check == 'n':
            break
        else:
            print('Invalid entry. Please try again. \n')
            
            
def main():
    while True:
        city, month, day = select_data()
        db_cty = load_data(city, month, day)
        time_info(db_cty)
        station_info(db_cty)
        trip_info(db_cty)
        bikers_info(db_cty)
        view_more(city, db_cty)
            
        repeat = input('\nContinue? y or n.\n')
        if repeat.lower() != 'y':
            break

if __name__ == "__main__":
    main()
