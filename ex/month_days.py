# Display no. of days in the given month

month = int(input("Enter month number :"))

ndays = 31

if month == 2:
    ndays = 28
elif month in [4, 6, 9, 11]:
    ndays = 30

print('No. of days =', ndays)
