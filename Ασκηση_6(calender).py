import datetime

            
calendar = [(31,'January'),
            (28,'Feburary'),
            (31,'March'),
            (30,'April'),
            (31,'May'),
            (30,'June'),
            (31,'July'),
            (31,'August'),
            (30,'September'),
            (31,'October'),
            (30,'November'),
            (31,'December') ]

Days =     [ (1,"Sunday"),
             (2,"Monday"),
             (3,"Tuesday"),
             (4,"Wednesday"),
             (5,"Thursday"),
             (6,"Friday"),
             (7,"Saturday")
             ]

calender=[]
days="S\t M\t T\t W\t T\t F\t S"


def is_leap():
    """Checks if year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

def make_calendar():

    if is_leap():
            calendar[1] = (29,'Feburary')

    start_pos=datetime.date(year,month,1)
    start=int(start_pos.strftime("%w"))
    mdays=calendar[month-1][0]
    month_name=calendar[month-1][1]
    counter=0

    for j in range(start):       
        calender.append(" ")
        calender.append('\t')
        counter+=1
    for i in range(1,mdays+1):
        calender.append(str(i))
        calender.append('\t')
        i+=1

    seira1=calender[0:14]
    seira2=calender[14:28]
    seira3=calender[28:42]
    seira4=calender[42:56]
    seira5=calender[56:70]
    seira6=calender[70:70+counter]
    
   
    print(month_name+" "+str(year))
    print(days)
    print(" ".join(seira1))
    print(" ".join(seira2))
    print(" ".join(seira3))
    print(" ".join(seira4))
    print(" ".join(seira5))
    print(" ".join(seira6))
    
year = int(input("Enter year:"))
month = int(input("Enter month:"))
button = input("Press C to create calendar \n")
if (button == "C" or button =="c"):
    make_calendar()
    

