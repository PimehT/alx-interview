#!/usr/bin/python3
"""
Adapted script to read stdin line by line and compute metrics,
with improved input handling and error management.
"""

import sys

# Initialize global variables
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
lines_processed = 0


def report_metrics(total_file_size, status_code_counts):
    """Report the accumulated metrics."""
    print(f"Total File Size: {total_file_size}")
    for status_code, count in status_code_counts.items():
        if count > 0:
            print(f"Status Code {status_code}: {count}")


try:
    for line in sys.stdin:
        # Skip empty lines and lines that don't match the expected format
        stripped_line = line.strip()
        if not stripped_line or len(stripped_line.split()) < 9:
            continue

        # Parse the line
        parts = stripped_line.split(maxsplit=8)
        if len(parts) < 9:
            continue

        # Extract and validate file size
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except (IndexError, ValueError):
            pass

        # Extract and validate status code
        try:
            status_code = int(parts[-2])
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except (IndexError, ValueError):
            pass

        lines_processed += 1

        # Report stats every 10 lines
        if lines_processed % 10 == 0:
            report_metrics(total_file_size, status_code_counts)

    # Report final stats
    report_metrics(total_file_size, status_code_counts)

except KeyboardInterrupt:
    report_metrics(total_file_size, status_code_counts)
    raise
