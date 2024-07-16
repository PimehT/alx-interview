#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """
import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        try:
            ip, ignore1, ignore2, date, method, url, protocol, status, size = parts
            status = int(status)
            size = int(size)
            if status in status_codes:
                status_codes[status] += 1
            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
        except ValueError:
            continue

    # Print any remaining stats after the loop
    print_stats()
