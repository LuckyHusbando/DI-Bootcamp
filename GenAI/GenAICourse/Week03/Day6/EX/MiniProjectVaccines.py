#MiniProjectVaccines

class Human:
    """
    Represents a citizen waiting for a vaccine.
    """
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        # Part 2: Initialize empty family list
        self.family = []

    def add_family_member(self, person: 'Human'):
        """Adds a person to this human's family and vice-versa."""
        # Ensure we avoid infinite loops or duplicates
        if person not in self.family:
            self.family = self.family + [person]
        if self not in person.family:
            person.family = person.family + [self]

    def __repr__(self):
        # Useful for printing and debugging
        return f"{self.name} (Age: {self.age}, Priority: {self.priority})"


class Queue:
    """
    Represents the vaccination queue.
    """
    def __init__(self):
        self.humans = []

    def add_person(self, person: Human):
        """Adds a human to the queue. Priority/Elderly go to index 0."""
        # Solved without list.insert()
        if person.age > 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans = self.humans + [person]

    def find_in_queue(self, person: Human):
        """Returns the index of a human."""
        # Solved without list.index()
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return None

    def swap(self, person1: Human, person2: Human):
        """Swaps the position of two humans in the queue."""
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        
        if idx1 is not None and idx2 is not None:
            self.humans[idx1], self.humans[idx2] = self.humans[idx2], self.humans[idx1]

    def get_next(self):
        """Returns and removes the first human in the queue."""
        # Solved without list.pop()
        if not self.humans:
            return None
            
        next_human = self.humans[0]
        self.humans = self.humans[1:]
        return next_human

    def get_next_blood_type(self, blood_type: str):
        """Returns and removes the first human with the specified blood type."""
        # Solved without list.pop() or list.index()
        if not self.humans:
            return None
            
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                target_human = self.humans[i]
                # Rebuild list skipping the found index
                self.humans = self.humans[:i] + self.humans[i+1:]
                return target_human
        return None

    def sort_by_age(self):
        """
        Sorts the queue: Priority people first, then descending by age.
        Implemented using Bubble Sort to avoid list.sort() or sorted().
        """
        n = len(self.humans)
        for i in range(n):
            for j in range(0, n - i - 1):
                p1 = self.humans[j]
                p2 = self.humans[j + 1]
                
                swap_needed = False
                
                # Rule 1: Priority True comes before Priority False
                if not p1.priority and p2.priority:
                    swap_needed = True
                # Rule 2: If priorities are the same, older comes before younger
                elif p1.priority == p2.priority:
                    if p1.age < p2.age:
                        swap_needed = True
                        
                if swap_needed:
                    # Swap the adjacent elements
                    self.humans[j], self.humans[j + 1] = self.humans[j + 1], self.humans[j]

    def rearrange_queue(self):
        """
        Rearranges the queue so no two family members are adjacent.
        """
        n = len(self.humans)
        for i in range(n - 1):
            current_person = self.humans[i]
            next_person = self.humans[i + 1]
            
            # If a family conflict is found
            if next_person in current_person.family:
                # Look ahead for someone who is not family to swap with
                for j in range(i + 2, n):
                    candidate = self.humans[j]
                    if candidate not in current_person.family:
                        self.swap(next_person, candidate)
                        break

#System Test#

if __name__ == "__main__":
    # Create humans
    alice = Human("1", "Alice", 30, False, "A")
    bob = Human("2", "Bob", 32, False, "B")
    charlie = Human("3", "Charlie", 70, False, "O")  # >60, should go to index 0 on insert
    diana = Human("4", "Diana", 25, True, "AB")      # Priority, should sort to front
    eve = Human("5", "Eve", 28, False, "A")

    # Part 2: Setup families
    # Alice and Bob are family.
    alice.add_family_member(bob)

    # Initialize queue
    q = Queue()
    
    # Test adding (Charlie should jump to index 0 because he is > 60)
    q.add_person(alice)
    q.add_person(bob)
    q.add_person(charlie)
    
    print("Queue after adds:")
    print(q.humans)
    # Output expected: Charlie, Alice, Bob
    
    # Test sorting
    q.add_person(diana) # jumps to 0
    q.add_person(eve)   # goes to end
    q.sort_by_age()
    
    print("\nQueue after sorting (Priority first, then Age):")
    print(q.humans)
    # Output expected: Diana (Priority), Charlie (70), Bob (32), Alice (30), Eve (28)

    # Test get_next_blood_type
    b_type_person = q.get_next_blood_type("B")
    print(f"\nPulled Blood Type B: {b_type_person.name}")
    print("Queue after pulling Bob:")
    print(q.humans)
    
    # Put Bob back right next to Alice to test family rearrangement
    q.humans = [alice, bob, charlie, diana, eve]
    print("\nQueue forced to have family (Alice & Bob) together:")
    print(q.humans)
    
    q.rearrange_queue()
    print("\nQueue after rearranging to separate family:")
    print(q.humans) 
    # Bob and Alice should no longer be adjacent