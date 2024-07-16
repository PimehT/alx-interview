#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""
import sys
import signal


def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats(total_size, status_codes)
    sys.exit(0)


if __name__ == "__main__":
    # Initialize variables
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    # Set up signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            # Extract size and status code
            try:
                size = int(parts[-1])
                status = int(parts[-2])
            except (IndexError, ValueError):
                continue

            # Update total size
            total_size += size

            # Update status code count if valid
            if status in status_codes:
                status_codes[status] += 1

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
