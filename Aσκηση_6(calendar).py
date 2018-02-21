import datetime 

calender = [('January', range(1, 31 + 1)),
            ('Feburary', range(1, 28 + 1)),
            ('March', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('May', range(1, 31 + 1)),
            ('June', range(1, 30 + 1)),
            ('July', range(1, 31 + 1)),
            ('August', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('October', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def make_calendar(year, start_day,month):
    # Determine current starting position on calendar
    start_pos = week.index(start_day)

    # if True, adjust Feburary date range for leap year | 29 days
    if is_leap(year):
        calender[1] = ('Feburary', range(1, 29 + 1))

    for month, days in calender:
        # Print month title
        print('{0} {1}'.format(month, year).center(20, ' '))
        # Print Day headings
        print(''.join(['{0:<3}'.format(w) for w in week]))
        # Add spacing for non-zero starting position
        print('{0:<3}'.format('')*start_pos, end='')

        for day in days:
            # Print day
            print('{0:<3}'.format(day), end='')
            start_pos += 1
            if start_pos == 7:
                # If start_pos == 7 (Sunday) start new line
                print()
                start_pos = 0 # Reset counter
        print('\n')

def is_leap(year):
    """Checks if year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

epilogi = input("If you want to make a calendar file press 'C' else press Enter \n")
if (epilogi == "C" or epilogi =="c"):
    firstdays = ["Mo", "Tu" , "We" , "Fr" , "Sa" , "Su" , "Mo" , "We" , "Th" , "Fr" , "Sa" ]
    for year, firstday in zip(range(2018,2029) , firstdays):
        make_calendar(year,firstday)
    print ("Rerun the programm")
else:
    check()




    

    
