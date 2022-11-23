import numpy as np
import pandas as pd
import time
pd.set_option('mode.chained_assignment',None)

def state():
    """
    chosing the state name of three washington, newyork and new york city
    """
    n = 0
    while True:
        if n == 0:
            print('Enter The state name, you have 3 options \nchicago \nnew york \nwashington')
        state_input = input('\n')
        state_input = state_input.lower()
        if state_input == 'new york':
            state_input = 'new_york_city'
        try:
            state_data = pd.read_csv(state_input + '.csv')
            return state_data, state_input
            break
        except:
            print('\nYou have entered a wrong state! \nPlease enter one of these three states with matching spellings \nchicago\nnew york\nwashington ')
        n+=1

def time_filter():
    """
    used for chosing the choice of filter which are for month and day
    """
    n = 0
    while True:
        if n==0:
            print('what do you want to filter out by month? day? or both? or even none?')
        filter_choice = input('\n')
        if filter_choice.lower() in ['month','day','both','none']:
            return filter_choice
            break
        else:
            print('wrong answer!\nplease enter one of the four following words with matching spellings:\nmonth \nday \nboth \nnone')
            n+=1

def filtering(filter_choice,state_data):
    """
    given filtered choice, filtering the data into right format
    """
    data_filtered = state_data
    if filter_choice in ['month','both']:
        while True:
            print('please enter a month from the following: jan, feb, mar, apr, may, jun')
            month_choice = input('\n')
            month_choice = month_choice.lower()
            if month_choice in ['jan','feb','mar','apr','may','jun']:
                if month_choice == 'jan':
                    m = '1'
                    nd = '31'
                elif month_choice == 'feb':
                    m = '2'
                    nd = '28'
                elif month_choice == 'mar':
                    m = '3'
                    nd = '31'
                elif month_choice == 'apr':
                    m = '4'
                    nd = '30'
                elif month_choice == 'may':
                    m = '5'
                    nd = '31'
                elif month_choice == 'jun':
                    m = '6'
                    nd = '30'
                data_filtered = data_filtered[(data_filtered['Start Time'] > ('2017-0'+m+'-01'+' 00:00:00')) & (data_filtered['Start Time'] < ('2017-0'+m+'-'+nd+' 23:59:59'))]
                break
            else:
                print('wrong answer!')
    if filter_choice in ['day','both']:
        while True:
            print('please enter a day from the following: sat, sun, mon, tue, wed, thu, fri')
            day_choice = input('\n')
            day_choice = day_choice.lower()
            if day_choice in ['sat','sun','mon','tue','wed','thu','fri']:
                if day_choice == 'sat':
                    day_name = 'Saturday'
                elif day_choice == 'sun':
                    day_name = 'Sunday'
                elif day_choice == 'mon':
                    day_name = 'Monday'
                elif day_choice == 'tue':
                    day_name = 'Tuesday'
                elif day_choice == 'wed':
                    day_name = 'Wednesday'
                elif day_choice == 'thu':
                    day_name = 'Thursday'
                elif day_choice == 'fri':
                    day_name = 'Friday'
                data_filtered = data_filtered[data_filtered['dayofweek'] == day_name]
                break
            else:
                print('invalid')
    return data_filtered


def calculations(filtered_data,filter_choice,state_choice):
    """
    doing all necessary calculations
    """
    state_filtered = filtered_data
    #1. popular times of travel calculation
    #---------------------------------------------------------
    #most common month if month is not chosen
    if filter_choice not in ['month','both']:
        start = time.time()
        most_common_months = state_filtered['Start Time'].dt.month.value_counts()
        most_common_month = most_common_months.index[[0][0]]
        count_of_most_common_month = most_common_months.iloc[[0][0]]
        print('The most common month is: {} with counts of {}'.format(most_common_month,count_of_most_common_month))
        print('(it took {} seconds)\n'.format(time.time()-start))

    #most common day of week if not chosen
    if filter_choice not in ['day','both']:
        start = time.time()
        most_common_dayofweeks = state_filtered['dayofweek'].value_counts()
        most_common_dayofweek = most_common_dayofweeks.index[[0][0]]
        count_of_most_common_dayofweek = most_common_dayofweeks.iloc[[0][0]]
        print('The most common day of week is: {} with counts of {}'.format(most_common_dayofweek,count_of_most_common_dayofweek))
        print('(it took {} seconds)\n'.format(time.time()-start))

    #most common hour
    start = time.time()
    state_filtered['hour'] = state_filtered['Start Time'].dt.hour
    most_common_hours = state_filtered['hour'].value_counts()
    most_common_hour = most_common_hours.index[[0][0]]
    count_of_most_common_hour = most_common_hours.iloc[[0][0]]
    print('The most common hour is: {} with counts of {}'.format(most_common_hour,count_of_most_common_hour))
    print('(it took {} seconds)\n'.format(time.time()-start))

    #2. Poular station and trips
    #----------------------------------------------------------

    #most common start location
    start = time.time()
    most_common_stlocs = state_filtered['Start Station'].value_counts()
    most_common_stloc = most_common_stlocs.index[[0][0]]
    count_of_most_common_stloc = most_common_stlocs.iloc[[0][0]]
    print('The most common start location is: {} with counts of {}'.format(most_common_stloc,count_of_most_common_stloc))
    print('(it took {} seconds)\n'.format(time.time()-start))

    #most common end location
    start = time.time()
    most_common_endlocs = state_filtered['End Station'].value_counts()
    most_common_endloc = most_common_endlocs.index[[0][0]]
    counts_of_most_common_endloc = most_common_endlocs.iloc[[0][0]]
    print('The most common end location is: {} with counts of {}'.format(most_common_endloc,counts_of_most_common_endloc))
    print('(it took {} seconds)\n'.format(time.time()-start))

    #most common Trip
    start = time.time()
    most_common_trips = state_filtered[['Start Station','End Station']].value_counts()
    most_common_trip_start = most_common_trips.index[[0][0]][0]
    most_common_trip_end = most_common_trips.index[[0][0]][1]
    count_of_most_common_trip = most_common_trips.iloc[[0][0]]
    print('The most common trip is: from {} to ----- {} with counts of {}'.format(most_common_trip_start,most_common_trip_end,count_of_most_common_trip))
    print('(it took {} seconds)\n'.format(time.time()-start))


    #3. Trip Duration
    #-------------------------------------------------------------------
    #total time and average time
    start = time.time()
    total_time = state_filtered['Trip Duration'].sum()
    total_count = state_filtered['Trip Duration'].count()
    average_for_trip = total_time/total_count
    print('The total trip time is {} with an average of {}'.format(total_time,average_for_trip))
    print('(it took {} seconds)\n'.format(time.time()-start))

    #4. User info
    #-------------------------------------------------------------

    #most common user
    start = time.time()
    most_common_user_types = state_filtered['User Type'].value_counts()
    most_common_user_type = most_common_user_types.index[[0][0]]
    count_of_most_common_user_type = most_common_user_types.iloc[[0][0]]
    print('The most common user type is: {} with counts of {}'.format(most_common_user_type,count_of_most_common_user_type))
    print('(it took {} seconds)\n'.format(time.time()-start))

    #most common gender and year of birth for NYC and chicago
    if state_choice in ['new_york_city','chicago']:
        #gender
        start = time.time()
        most_common_genders = state_filtered['Gender'].value_counts()
        most_common_gender = most_common_genders.index[[0][0]]
        count_of_most_common_gender = most_common_genders.iloc[[0][0]]
        print('most common gender is {} with counts of {}'.format(most_common_gender,count_of_most_common_gender))
        print('(it took {} seconds)\n'.format(time.time()-start))

        #date of birth
        start = time.time()
        most_common_dateofbirths = state_filtered['Birth Year'].value_counts()
        most_common_dateofbirth = most_common_dateofbirths.index[[0][0]]
        count_of_most_common_dateofbirth = most_common_dateofbirths.iloc[[0][0]]
        maximun_age = most_common_dateofbirths.index.min()
        minimum_age = most_common_dateofbirths.index.max()
        print('The most common date of birth is {} with counts of {}'.format(most_common_dateofbirth,count_of_most_common_dateofbirth))
        print('The most recent date of birth is {} and earliest is {}'.format(minimum_age,maximun_age))
        print('(it took {} seconds)\n'.format(time.time()-start))



def data_preview(state_filtered):
    """
    previewing 5 raw data at a time for the user
    """
    filtered_data = state_filtered.reset_index(drop=True)
    n = 0
    start_row = 0
    end_row = 5
    while True:
        if n ==0:
            print('would you like to see some raw data?\n please write yes or no')
        preview = input('\n')
        preview = preview.lower()
        if preview in ['yes','no']:
            if preview == 'no':
                break
            elif preview == 'yes':
                print('here are 5 rows for your display:')
                print(filtered_data.loc[start_row:end_row,:])
                print('would you like to see more 5 rows? please write either yes or no')
                n+=1
                start_row+=5
                end_row+=5
        else:
            print('wrong answer!, please write either yes or no')
            n+=1

def main():
    n = 0
    while True:
        if n==0:
            #calling for state name from user
            state_data, state_choice = state()
            #data cleaning
            state_data = state_data.rename(columns = {'Unnamed: 0':'ID'})
            state_data['Start Time'] = pd.to_datetime(state_data['Start Time'])
            state_data['End Time'] = pd.to_datetime(state_data['End Time'])
            state_data['dayofweek'] = state_data['Start Time'].dt.day_name()
            #calling for filter specification
            filter_choice = time_filter()
            #applying filter to the data
            state_filtered = filtering(filter_choice,state_data)
            #doing the calculations
            calculations(state_filtered,filter_choice,state_choice)
            #previewing the data
            data_preview(state_filtered)
            #looping over for restarting or closing the program
        answer = input('This is the end of the program, do you want to restart?\n write yes or no\n')
        if answer.lower() in ['yes','no']:
            if answer == 'no':
                break
            elif answer == 'yes':
                n = 0
        else:
            print('please enter a valid expression')
            n+=1



if __name__ == "__main__":
    main()
