#!/usr/bin/python3

import sys

def print_stats(status_counts, total_file_size):
    """
    Print statistics for status codes and total file size.
    Args:
        status_counts (dict): Dictionary containing counts of each status code.
        total_file_size (int): Total file size.
    """
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """
    Parse a log line and extract status code and file size.
    Args:
        line (str): Log line.
    Returns:
        tuple: (status_code, file_size) if line is valid, otherwise (None, None).
    """
    parts = line.split()
    if len(parts) >= 7 and parts[-3] == "GET":
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            return status_code, file_size
        except ValueError:
            pass
    return None, None

def main():
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1
            if line_count == 10:
                print_stats(status_counts, total_file_size)
                line_count = 0
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(status_counts, total_file_size)

if __name__ == "__main__":
    main()
