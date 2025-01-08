import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
def calculate_future_date():
    # Asking the user for the number of days to add
    days_to_add = int(input('Enter the number of days to add to the current date: '))
    
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate the future date
    calculate_future_date()
    
    print('Thank you for using the date and time calculator.')
    
    # # Ask the user if they want to calculate the future date
    # calculate_future_date_choice = input('Do you want to calculate the future date? (yes/no): ')
    
    # if calculate_future_date_choice.lower() == 'yes':
    #     calculate_future_date()
    # else:
    #     print('Thank you for using the date and time calculator.')

if __name__ == "__main__":
    main()