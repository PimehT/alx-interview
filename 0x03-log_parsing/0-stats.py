#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def display_metrics(total_size, status_count):
    """Print accumulated metrics. """
    print(f"File size: {total_size}")
    for status in sorted(status_count):
        print(f"{status}: {status_count[status]}")


if __name__ == "__main__":
    import sys

    total_size = 0
    status_count = {}
    valid_status_codes = [
        '200', '301', '400', '401', '403', '404', '405', '500'
    ]
    line_counter = 0

    try:
        for line in sys.stdin:
            if line_counter == 10:
                display_metrics(total_size, status_count)
                line_counter = 1
            else:
                line_counter += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_status_codes:
                    if status_count.get(parts[-2]) is None:
                        status_count[parts[-2]] = 1
                    else:
                        status_count[parts[-2]] += 1
            except IndexError:
                pass

        display_metrics(total_size, status_count)

    except KeyboardInterrupt:
        display_metrics(total_size, status_count)
        raise
