#!/usr/bin/env python3

"""
implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the
project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should
be returned.
"""
from typing import Tuple, List
import csv
import math


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        :param page: page number
        :param page_size: size of the page
        :return: a list of elements (lists) in the wanted page
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        items_range = index_range(page, page_size)
        data = self.dataset()

        return data[items_range[0]: items_range[1]]
