"""
RECORD CHECK  -  my version
===========================

Name  :  Mikaeil Nikookar
Lane  :  IT
Date  :  12/11/2026

Run it:   python template.py

Reads messy server lines from raw_servers.txt, cleans each one into a dict,
prints it with its status, then prints a summary.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy server line and return it as a dict."""
    line = raw_line.strip().lower()
    hostname, rest = line.split(",", 1)

    used_part, total_part = rest.split(",")
    used_key, used = used_part.split("=")
    total_key, total = total_part.split("=")

    return {
        "hostname": hostname.strip(),
        "used": float(used.strip()),
        "total": float(total.strip()),
    }


def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# =============================================================== INPUT + OUTPUT

count = 0
flagged = 0

with open("raw_servers.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        status = status_of(record["used"], record["total"])
        print(record, status)

        count = count + 1
        if status != "OK":
            flagged = flagged + 1

print()
print(f"{count} records, {flagged} flagged")
