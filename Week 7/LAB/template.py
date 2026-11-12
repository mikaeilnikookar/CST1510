"""
RECORD CHECK  -  my version
===========================

Name  :  Mikaeil Nikookar
Lane  :  IT
Date  :  12/11/2026

Run it:   python template.py

Reads messy server status lines from raw_servers.txt
("  Srv-01 , used=87 , total=100  "), cleans and parses each one into a dict,
prints it with its status, and ends with a one-line summary.
"""

DATA_FILE = "raw_servers.txt"

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy 'hostname, used=.., total=..' line into a dict."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return {"hostname": hostname_part.strip(), "used": fields["used"], "total": fields["total"]}


def status_of(used, total):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def load_raw_lines(path):
    """Return every non-blank raw line from a file, uncleaned."""
    raw_lines = []
    with open(path) as f:
        for line in f:
            if line.strip():
                raw_lines.append(line)
    return raw_lines


# ====================================================================== INPUT

raw_records = load_raw_lines(DATA_FILE)


# =============================================================== PROCESS + OUTPUT

total_count = 0
flagged_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
    except (ValueError, KeyError):
        # e.g. "used=unknown" -> ValueError: could not convert string to float
        print(f"Could not parse: {raw_record.strip()}")
        continue

    status = status_of(record["used"], record["total"])
    print(f"{status:<11} {record}")

    total_count += 1
    if status != "OK":
        flagged_count += 1

print()
print(f"{total_count} records parsed, {flagged_count} flagged (WARNING or OVER LIMIT)")
