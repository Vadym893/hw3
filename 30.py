
time_24_hour = input("Enter time (24-hour format, hh:mm): ")

hour, minute = map(int, time_24_hour.split(':'))

period = "am" if hour < 12 else "pm"

if hour == 0:
    hour_12_hour = 12
elif hour > 12:
    hour_12_hour = hour - 12
else:
    hour_12_hour = hour

time_12_hour = f"{hour_12_hour}:{minute:02d}{period}"
print("Time in 12-hour format:", time_12_hour)
