
####This version came recommend from another developer as a way to seperate data collection from the class itself. It was explained to me that this is best practice

class User:
    def __init__(self, date, name, phone, shells, taps):
        self.date = date
        self.name = name
        self.phone = phone
        self.shells = shells
        self.taps = taps
        self.total = (shells * 100) + (taps * 50)
        swaps = []
        self.swaps = swaps


def change_value(self):
        nshells = int(input("enter the new number of kegs:  "))
        ntaps = int(input("Enter new number of taps: "))
        self.shells = nshells
        self.taps = ntaps
        self.total = (nshells * 100) + (ntaps * 50)
        print(
            f"Number of shells changed to {self.shells}\nNumber of taps changed to {self.taps}\nNew total set to ${self.total}")

    def add_record(self):
        new_record = input("Enter Swap Record DD/MM/YYYY")
        self.swaps.append(new_record)
        print(f"Swap Log:  {self.swaps}")

    def show_all(self):
        print(f"Date started: {self.date}\nName: {self.name}\nPhone Number: {self.phone}\nNumber of shells: {self.shells}\nNumber of taps: {self.taps}\nTotal amount on hold: ${self.total}\nSwap dates{self.swaps}")

    def keg_return(self):
        returned_shells = int(input("Input the number of shells refunded:  "))
        self.shells -= returned_shells
        self.total = (self.shells * 100) + (self.taps * 50)
        print(
            f"You have changed the number of shells to {self.shells}\nYour new total is {self.total}")

    def tap_return(self):
        returned_taps = int(
            input("Enter the number of taps you are returning:  "))
        self.taps -= returned_taps
        self.total = (self.taps * 50) + (self.shells * 100)
        print(
            f"you have changed the number of taps to: {self.taps}\nYour total is now: {self.total}")


date = input('Enter the date:  ')
name = input('Enter the full name: ')
phone = input("Enter the phone number: ")
shells = input('Enter the number of shells:    ')
taps = input('Enter the number of taps:    ')

user: User = User(date, name, phone, shells, taps)
