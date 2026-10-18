"""
RECORD CHECK  -  my version
===========================

Name  :  Mikaeil Nikookar
Lane  :  IT
Date  :  19/10/2026

Run it:   python template.py

Total of 0 -> ZeroDivisionError: division by zero
              (in check(), percent = (value / limit) * 100 divides by 0)
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage used."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the GB free and the percentage used."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def print_summary(over_limit_count):
    """Print how many records came back OVER LIMIT."""
    print()
    print(f"Records OVER LIMIT this session: {over_limit_count}")


# ====================================================================== MAIN

over_limit_count = 0

while True:
    # ================================================================ INPUT
    label = input("Hostname (or quit): ")
    if label == "quit":
        break
    value = float(input("GB used  : "))
    limit = float(input("GB total : "))

    # ============================================================== PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1

    # =============================================================== OUTPUT
    print_report(label, value, limit, difference, percent, status)

print_summary(over_limit_count)
