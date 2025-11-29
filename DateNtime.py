# checking leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Days in month
def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


# Function to count days from year 0 to given date
def days_from_start(d, m, y):
    days = 0

    # Add days for full past years
    for yr in range(0, y):
        days += 366 if is_leap(yr) else 365

    # Add days for full months of current year
    for mn in range(1, m):
        days += days_in_month(mn, y)

    # Add days in current month
    days += d

    return days


# Input
dob_d = int(input("Birth Day: "))
dob_m = int(input("Birth Month: "))
dob_y = int(input("Birth Year: "))

# Input today's date
cur_d = int(input("Current Day: "))
cur_m = int(input("Current Month: "))
cur_y = int(input("Current Year: "))

# Convert both dates into "total days since year 0"
dob_days = days_from_start(dob_d, dob_m, dob_y)
cur_days = days_from_start(cur_d, cur_m, cur_y)

# Total days lived
total_days = cur_days - dob_days

# Years lived (just to display)
years = cur_y - dob_y
if (cur_m < dob_m) or (cur_m == dob_m and cur_d < dob_d):
    years -= 1

# Hours lived
hours = total_days * 24

print("Years lived:", years)
print("Days lived:", total_days)
print("Hours lived:", hours)