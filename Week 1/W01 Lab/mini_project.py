# Week 1 mini-project - Record Check
# Lane: IT (hostname, GB used, GB total)

# INPUT - ask for the three values and convert the numbers
hostname = input("Hostname : ")
gb_used = float(input("GB used  : "))
gb_total = float(input("GB total : "))

# PROCESS - calculate what you were not given
gb_free = gb_total - gb_used
percent_used = (gb_used / gb_total) * 100

# Why: monitoring tools usually raise an alert when a disk reaches 90% full,
# so this shows how many GB can still be written before that alert fires.
alert_percent = 90
gb_before_alert = (gb_total * alert_percent / 100) - gb_used

# OUTPUT - print the bordered report
border = "=" * 34

print(border)
print(f"  RECORD CHECK  -  {hostname}")
print(border)
print(f"  Used        : {gb_used:>10.2f}")
print(f"  Total       : {gb_total:>10.2f}")
print(f"  Free        : {gb_free:>+10.2f}")
print(f"  Percent     : {percent_used:>10.2f} %")
print(f"  Before alert: {gb_before_alert:>+10.2f}")
print(border)
