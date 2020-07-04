from car_rental_GitHub import *

#set up a honda accord
honda_accord = Car(2019, "Honda", "Accord", "Sedan", 30)
#set up calendar for Honda Accord
honda_accord_calendar = honda_accord.Calendar(25)

#set up a nissan altima
nissan_altima = Car(2020, "Nissan", "Altima", "Sedan", 33.5)
#set up calendar for Nissan Altima
nissan_altima_calendar = nissan_altima.Calendar(25)

#set up a Toyota Rav4
toyota_rav4 = Car(2019, "Toyota", "Rav4", "Crossover", 30.5)
#set up calendar for Toyota Rav4
toyota_rav4_calendar = toyota_rav4.Calendar(35)

#we know have three cars set up. Below are tests for each one.
#dictionary for test results
test_results = {"right": 0, "total":0}
def right():
    test_results["right"] += 1
    test_results["total"] += 1
def wrong():
    test_results["total"] += 1


#honda accord tests
#basic single month reservation, March 1 to March 8
honda_accord_calendar.reserve("March", 1, "March", 8)
#it worked
right()
#copy to ensure it got blocked off
honda_accord_calendar.reserve("March", 1, "March", 8)
#it worked
right()

#rinse and repeat for different days
honda_accord_calendar.reserve("June", 2, "June", 14)
right()
honda_accord_calendar.reserve("June", 2, "June", 14)
right()
honda_accord_calendar.reserve("October", 4, "October", 27)
right()
honda_accord_calendar.reserve("October", 4, "October", 27)
right()

#two month reservations
honda_accord_calendar.reserve("January", 2, "February", 10)
right()
honda_accord_calendar.reserve("January", 2, "February", 10)
right()
honda_accord_calendar.reserve("November", 23, "December", 1 )
right()
honda_accord_calendar.reserve("November", 23, "December", 1 )
right()
honda_accord_calendar.reserve("October", 31, "November", 1)
right()
honda_accord_calendar.reserve("October", 31, "November", 1)
right()

#test nissan altima
#basic reservations
nissan_altima_calendar.reserve("January", 1, "January", 6)
right()
nissan_altima_calendar.reserve("January", 1, "January", 6)
right()
nissan_altima_calendar.reserve("January", 7, "January", 8)
right()
nissan_altima_calendar.reserve("January", 7, "January", 8)
right()
nissan_altima_calendar.reserve("January", 10, "January", 31)
right()
nissan_altima_calendar.reserve("January", 10, "January", 31)
right()

#test of reservations beginning and ending in different months
nissan_altima_calendar.reserve("February", 1, "March", 1)
right()
nissan_altima_calendar.reserve("February", 1, "March", 1)
right()
nissan_altima_calendar.reserve("March", 2, "April", 2)
right()
nissan_altima_calendar.reserve("March", 2, "April", 2)
right()
nissan_altima_calendar.reserve("April", 3, "May", 3)
right()
nissan_altima_calendar.reserve("April", 3, "May", 3)
right()

#tests of Toyota Rav4... Final Tests!!!!!
#basic test
toyota_rav4_calendar.reserve("January", 1, "January", 20)
right()
toyota_rav4_calendar.reserve("January", 1, "January", 20)
right()
toyota_rav4_calendar.reserve("January", 21, "January", 31)
right()
toyota_rav4_calendar.reserve("January", 21, "January", 31)
right()
toyota_rav4_calendar.reserve("February", 1, "February", 28)
right()
toyota_rav4_calendar.reserve("February", 1, "February", 28)
right()

#two month tests
toyota_rav4_calendar.reserve("March", 1, "April", 1)
right()
toyota_rav4_calendar.reserve("March", 1, "April", 1)
right()
toyota_rav4_calendar.reserve("April", 2, "May", 2)
right()
toyota_rav4_calendar.reserve("April", 2, "May", 2)
right()
toyota_rav4_calendar.reserve("May", 3, "June", 5)
right()
toyota_rav4_calendar.reserve("May", 3, "June", 5)
right()

print("Correct rate:")
print(test_results["right"]/test_results["total"])
