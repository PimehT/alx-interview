#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
- Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- Prints statistics after every 10 lines and upon keyboard
interruption (CTRL + C).
"""
import sys


# Initialize global variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        # Extract file size
        try:
            size = int(parts[-1])
            total_size += size
        except (IndexError, ValueError):
            continue

        # Extract status code
        try:
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            continue

        line_count += 1

        # Print stats every 10 lines
        if line_count == 10:
            print_stats(total_size, status_codes)
            line_count = 0

    # Print any remaining stats after the loop
    print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
