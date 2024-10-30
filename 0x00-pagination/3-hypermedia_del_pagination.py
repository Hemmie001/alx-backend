#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            """truncated_dataset = dataset[:1000]"""
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination data.
        
        Args:
            index (int, optional): The starting index of the page. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.
        
        Returns:
            Dict: A dictionary containing the index, next_index, page_size, and data.
        
        Raises:
            AssertionError: If the index is out of valid range.
        """
        dataset = self.indexed_dataset()

        # Assert that index is in a valid range
        if index is not None:
            assert 0 <= index < len(dataset), "Index is out of range"

        # If no index is provided, start from the beginning
        if index is None:
            index = 0

        # Create a list to hold the page data
        page_data = []
        
        # Track the current index for the dataset
        current_index = index
        total_items = len(dataset)

        # Gather page_data and find the next valid index
        while len(page_data) < page_size and current_index < total_items:
            # Check if the current index exists in the dataset
            if current_index in dataset:
                page_data.append(dataset[current_index])
            current_index += 1

        # The next index to query
        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': page_data,
        }
