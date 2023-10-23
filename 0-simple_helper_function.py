#!/usr/bin/env python3

"""
Write a function named index_range that takes two integer arguments page and
page_size.

The function should return a tuple of size two containing a start index and
an end index corresponding to the range of indexes to return in a list for
those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a function that calculates the start index and end index for pagination
    :param page: page number
    :param page_size: allowed elements count in the page
    :return: a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
