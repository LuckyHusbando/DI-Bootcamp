#Daily Challenge - Pagination

import math

class Pagination:
    """A class to handle paginated content."""

    def __init__(self, items=None, page_size=10):
        """
        Initializes the Pagination object.
        
        Args:
            items (list, optional): The list of items to paginate. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.
        """
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        
        # Calculate total number of pages. Handles empty list case.
        if len(self.items) == 0:
            self.total_pages = 1
        else:
            self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """
        Returns the list of items visible on the current page.
        
        Returns:
            list: A list of items for the current page.
        """
        start_index = self.current_idx * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def go_to_page(self, page_num):
        """
        Navigates to a specified page number (1-based).
        
        Args:
            page_num (int): The page number to go to.
        
        Raises:
            ValueError: If the page number is out of the valid range.
        """
        page_idx = page_num - 1
        if not (0 <= page_idx < self.total_pages):
            raise ValueError(f"Page number {page_num} is out of range. Valid pages are 1 to {self.total_pages}.")
        self.current_idx = page_idx

    def first_page(self):
        """Navigates to the first page."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Navigates to the last page."""
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """Moves one page forward."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Moves one page backward."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """Returns a string representation of the current page's items."""
        visible_items = self.get_visible_items()
        return '\n'.join(visible_items)


# Step 6: Test Your Code
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("--- Test 1: Initial State ---")
print(p.get_visible_items())
# Expected: ['a', 'b', 'c', 'd']

print("\n--- Test 2: Next Page ---")
p.next_page()
print(p.get_visible_items())
# Expected: ['e', 'f', 'g', 'h']

print("\n--- Test 3: Last Page ---")
p.last_page()
print(p.get_visible_items())
# Expected: ['y', 'z']

print("\n--- Test 4: Go To Page (Valid) ---")
# The total number of pages is ceil(26/4) = 7.
# Going to page 7 sets the internal index to 6.
p.go_to_page(7)
print(p.current_idx + 1)
# Expected: 7

print("\n--- Test 5: Go To Page (Invalid) ---")
try:
    p.go_to_page(10)
except ValueError as e:
    print(f"Error caught as expected: {e}")
# Expected: Raises ValueError

print("\n--- Test 6: Go To Page (Invalid, 0-based) ---")
try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Error caught as expected: {e}")
# Expected: Raises ValueError

print("\n--- Test 7: `__str__` Method ---")
p.first_page()
print(str(p))
# Expected output on new lines:
# a
# b
# c
# d