class WeeklySales:
    days_of_week = { 'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6 }

    def __init__(self, *args):
        # sales numbers for Mon thru Sat
        self.weekly_sales = list(args)
        # Sunday is closed
        self.weekly_sales.append(0)

    def __getattr__(self, day):
        day = day.lower()
        if day in self.days_of_week:
            return self.weekly_sales[self.days_of_week[day]]
        else:
            raise AttributeError('{} is not a valid day of the week'.format(day))

    def total(self):
        return sum(self.weekly_sales)


this_week = WeeklySales(22, 27, 30, 29, 38, 44)
print('Tuesday sales: {}'.format(this_week.Tue))
print('Total sales: {}'.format(this_week.total()))
# correct Tuesday sales
this_week.Tue = 31
print('Tuesday sales: {}'.format(this_week.Tue))
print('Total sales: {}'.format(this_week.total()))

