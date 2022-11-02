from datetime import datetime

class DateHandler:
    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date
    def format_date(self):
        return self.strftime("%Y/%m/%d")
    def get_days_between(self):
        return (self.end_date - self.start_date).days

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

obj = DateHandler(start_date, end_date)

print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:",obj.get_days_between())

