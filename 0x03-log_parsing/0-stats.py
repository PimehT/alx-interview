#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """
import re
import signal
import sys

# Initialize variables
total_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

# Regex pattern to parse log lines
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
    r'"GET /projects/260 HTTP/1\.1" (?P<status>\d+) (?P<size>\d+)'
)


def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(signum, frame):
    """Handle SIGINT (Ctrl+C)"""
    print_stats()
    sys.exit(0)


# Register signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        size = int(match.group("size"))
        status = int(match.group("status"))

        total_size += size
        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

# Print final stats if the script ends normally
print_stats()
