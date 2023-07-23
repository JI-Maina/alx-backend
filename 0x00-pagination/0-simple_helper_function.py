#!/usr/bin/env python3
"""
Defines a function named index_range that takes two integer arguments page and
page_size
"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters"""

    start_idx = 0
    end_idx = page_size

    if page <= 1:
        return (start_idx, end_idx)

    for _ in range(page - 1):
        start_idx = start_idx + page_size
        end_idx = end_idx + page_size

    return (start_idx, end_idx)
