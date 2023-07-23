import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
    """

    start_idx = 0
    end_idx = page_size

    if page <= 1:
        return (start_idx, end_idx)

    for _ in range(page - 1):
        start_idx = start_idx + page_size
        end_idx = end_idx + page_size

    return (start_idx, end_idx)


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
        """return the appropriate page of the dataset"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)

        pages = []

        if self.__dataset is None:
            self.dataset()

        for key, page in enumerate(self.__dataset):
            if key >= start_idx and key < end_idx:
                pages.append(page)

        return pages
