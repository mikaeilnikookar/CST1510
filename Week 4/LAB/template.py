"""
RECORD CHECK  -  my version
===========================

Name  :  Mikaeil Nikookar
Lane  :  IT
Date  :  19/10/2026

Run it:   python template.py

Reads servers.txt (hostname,GB used,GB total), prints a report for each
server, and writes hostname,status lines to results.txt.
"""

DATA_FILE = "servers.txt"
RESULTS_FILE = "results.txt"

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return the GB free, the percentage used and the status."""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one server."""
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


def print_message(text):
    """Print a one-line message on its own, with a blank line before it."""
    print()
    print(text)


def load_records(path):
    """Read hostname,used,total lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


# ====================================================================== STORE

try:
    records = load_records(DATA_FILE)
except FileNotFoundError:
    print_message(f"Could not find {DATA_FILE} - starting with no records")
    records = []


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

with open(RESULTS_FILE, "w") as results:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        if status == "OVER LIMIT":
            over_limit_count += 1
        print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)
        results.write(f"{record['label']},{status}\n")

print_message(f"{over_limit_count} of {len(records)} servers were OVER LIMIT "
              f"- results written to {RESULTS_FILE}")
