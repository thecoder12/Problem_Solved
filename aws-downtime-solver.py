seconds_in_yr = 60*60*24*365 ## seconds in a year
print(seconds_in_yr)
secs_downtime = seconds_in_yr//0.99999 # 99.999% uptime guaranteed by AWS.
downtime_secs = secs_downtime - seconds_in_yr # seconds downtime of AWS in a year
print(str(downtime_secs) + 'secs downtime in a year')
print(str(downtime_secs/(60)) + 'mins downtime in a year') # mins downtime of AWS in a year
