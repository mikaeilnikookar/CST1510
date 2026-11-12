"""
RECORD CHECK  -  my version
===========================

Name  :  Mikaeil Nikookar
Lane  :  IT
Date  :  12/11/2026

Run it:   python template.py

Loads servers from servers.txt (hostname,GB used,GB total) as Server objects,
prints a bordered report for each one with its status, and counts how many
servers are OVER LIMIT.
"""

DATA_FILE = "servers.txt"

# ====================================================================== CLASS

class Server:
    """One server: its hostname, GB used and GB total."""

    def __init__(self, hostname, used, total):
        """Store the three fields on this object."""
        self.hostname = hostname
        self.used = used
        self.total = total

    def free(self):
        """Return the GB still free on this server."""
        return self.total - self.used

    def percent(self):
        """Return GB used as a percentage of GB total."""
        return (self.used / self.total) * 100

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK, using percent()."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read hostname,used,total lines from a file and return a list of Servers."""
    servers = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            hostname, used, total = line.split(",")
            servers.append(Server(hostname, float(used), float(total)))
    return servers


def print_report(server, status):
    """Print the bordered report for one server."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {server.hostname}")
    print("=" * 34)
    print(f"  Used (GB)   : {server.used:>10.2f}")
    print(f"  Total (GB)  : {server.total:>10.2f}")
    print(f"  Free (GB)   : {server.free():>10.2f}")
    print(f"  Percent     : {server.percent():>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


records = load_records(DATA_FILE)


# ==================================================================== OUTPUT

over_limit_count = 0

for record in records:
    status = record.status()          # called once, stored, then reused
    print_report(record, status)
    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} of {len(records)} servers are OVER LIMIT")
