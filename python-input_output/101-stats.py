#!/usr/bin/python3
"""Read stdin line by line and compute metrics."""

import sys


def print_stats(total_size, counts):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(counts.keys()):
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def main():
    """Process stdin, print stats every 10 lines and at the end."""
    total_size = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    counts = {c: 0 for c in codes}
    i = 0
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                status = parts[-2]
                size = parts[-1]
                try:
                    total_size += int(size)
                except Exception:
                    pass
                if status in counts:
                    counts[status] += 1
            i += 1
            if i % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise
    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
