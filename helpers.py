from datetime import date, timedelta


def last_day_of_quarter(year, quarter):
    last_month_of_quarter = quarter * 3 
    if last_month_of_quarter == 12:
        return date(year, 12, 31)  
    
    first_day_next_month = date(year, last_month_of_quarter + 1, 1)  
    last_day = first_day_next_month - timedelta(days=1)  
    return last_day