#car rental Github portfolio
#class for a standard car
class Car:
    def __init__(self, year, brand, model, build_type, mpg):
        self.year = year
        self.brand = brand
        self.model = model
        self.build_type = build_type
        self.mpg = mpg
    class Calendar():
        def __init__(self, daily_rate):
            self.booked_days_month = {"January":[], "February": [], "March": [], "April": [], "May":[], "June":[], "July":[], "August":[], "September":[], "October":[], "November":[], "December":[]}
            self.daily_rate = daily_rate
        def reserve(self, start_month, start_day, end_month, end_day):
            self.month_length = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November":30, "December": 31}
            self.month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            self.start_month = start_month
            self.start_day = start_day
            self.end_month = end_month
            self.end_day = end_day
            reservation_complete = True
            self.days_of_month_reserved = self.booked_days_month[start_month]
            if (self.start_month == self.end_month):
                #this just got a whole lot easier
                self.reserve_days = []
                self.starting_day = self.start_day
                while (self.starting_day <= self.end_day):
                    self.reserve_days.append(self.starting_day)
                    self.starting_day += 1
                self.total_days = len(self.reserve_days)
                for self.day in self.reserve_days:
                    for self.booked_day in self.booked_days_month[self.start_month]:
                        if (self.day == self.booked_day):
                            reservation_complete = False
                if (reservation_complete == True):
                    reservation_message = "Reservation complete. You will pay a total price of " + str(self.daily_rate * (self.total_days))
                    for self. reserve_day in self.reserve_days:
                        self.booked_days_month[self.start_month].append(self.reserve_day)
                else:
                    reservation_complete = False
                self.reserve_days.clear()

            else:
                if (self.month_order.index(self.end_month) - self.month_order.index(self.start_month) == 1):
                    self.month_one_days = []
                    self.starting_day = self.start_day
                    while (self.starting_day <= self.month_length[self.start_month]):
                        self.month_one_days.append(self.starting_day)
                        self.starting_day += 1
                    self.month_two_days = []
                    self.starting_day = 1
                    while (self.starting_day <= self.end_day):
                        self.month_two_days.append(self.starting_day)
                        self.starting_day += 1
                    self.total_days = len(self.month_one_days) + len(self.month_two_days) 
                    self.cost = self.total_days * self.daily_rate
                    for self.month_one_day in self.month_one_days:
                        for self.booked_day in self.booked_days_month[self.start_month]:
                            if (self.booked_day == self.month_one_day):
                                reservation_complete = False
                    for self.month_two_day in self.month_two_days:
                        for self.booked_day in self.booked_days_month[self.end_month]:
                            if (self.booked_day == self.month_two_day):
                                reservation_complete = False
                    if (reservation_complete == True):
                        reservation_message = "Reservation complete. You will pay a total price of " + str(self.cost)
                        for self.month_one_day in self.month_one_days:
                            self.booked_days_month[self.start_month].append(self.month_one_day)
                        for self.month_two_day in self.month_two_days:
                            self.booked_days_month[self.end_month].append(self.month_two_day)
                    self.month_one_days.clear()
                    self.month_two_days.clear()
                else:
                    reservation_complete = False
            if (reservation_complete == False):
                reservation_message = "Sorry, there was an error in the reservation process. Please try again with different dates or a different car."
            print(reservation_message) 
def __main__():
    pass
if __name__ == "__main__":
    __main__()

