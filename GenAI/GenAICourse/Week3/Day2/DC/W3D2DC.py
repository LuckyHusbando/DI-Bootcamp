#W3D2DC

#Daily Challenge:

import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        #If none given, empty list
        self.items = items if items is not None else []

        #page_size must be integer, default 10 if invalid
        self.page_size = int(page_size)
        self.current_idx = 0

        #Calculate total pages dynamically
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 1

    def get_visible_items(self):
        """Returns the slice of items visible on the current page index."""
        #Calculate starting and ending indices for slicing
        start_idx = self.current_idx * self.page_size
        end_idx = start_idx + self.page_size

        #Return sliced subset of items
        return self.items[start_idx:end_idx]
    
    #Navigation methods

    def go_to_page(self, page_num):
        """Goes to the specified 1-based page number."""
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} is out of bounds. It must be between 1 and {self.total_pages}.")
    
    #Convert 1-based user input back to 0-based index
        self.current_idx = page_num - 1

    def first_page(self):
        """Navigates to the first page."""
        self.current_idx = 0
        return self
    
    def last_page(self):
        """Navigates to the last page."""
        #Total pages at least 1, so subtracting 1 gives us the corrent final index.
        self.current_idx = self.total_pages - 1
        return self
    
    def next_page(self):
        """Moves one page forward if not already on the last page."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self
    
    def previous_page(self):
        """Moves one page backward if not already on first page."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    #Custom __str__ method

    def __str__(self):
        """Returns a string of current page's items, separated by newlines."""
        visible_items = self.get_visible_items()

        #Convert item to string (safeguard) and join with newline
        return "\n".join(str(item) for item in visible_items)
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

print("\n--- Testing Errors ---")

try:
    p.go_to_page(10)
except ValueError as e:
    print(f"Caught an error: {e}")
# Output: ValueError

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Caught an error: {e}")
# Raises ValueError