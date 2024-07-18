#!/usr/bin/python3
"""Import required module"""
import sys


def print_statistics(total_file_size, status_codes):
    """
    Print metrics including total file size and status code counts.
    """
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):
    """Parse a line and extract file size and status code."""
    parts = line.split()  # split line into components
    if len(parts) >= 7:
        file_size_str = parts[-1]
        code_str = parts[-2]
        # check if the status code(code_str) is in the allowed list
        # of strings (status_codes)
        if code_str in status_codes:
            try:
                # convert file_size to integer or try to, lol
                file_size = int(file_size_str)
                return file_size, code_str
            except ValueError:
                # Handle case where file size is not an integer
                return None, None
    return None, None


if len(parts) >= 7:
        file_size_str = parts[-1]
        code_str = parts[-2]
        # check if the status code(code_str) is in the allowed list
        # of strings (status_codes)
        if code_str in status_codes:
            try:
                # convert file_size to integer or try to, lol
                file_size = int(file_size_str)
                return file_size, code_str
            except ValueError:
                # Handle case where file size is not an integer
                return None, None
    return None, None
