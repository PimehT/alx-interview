#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""
import sys
import signal


def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats(total_size, status_codes)
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    # Initialize variables
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)
            except ValueError:
                continue
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)
