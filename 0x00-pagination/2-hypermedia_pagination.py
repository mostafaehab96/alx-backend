#!/usr/bin/env python3

"""
Implement a get_hyper method that takes the same arguments (and defaults) as
get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""
from typing import Tuple, List, Dict
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """Calculates data for Hypermedia pagination"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        metrics = {
            "page": page,
            "page_size": len(data),
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return metrics
