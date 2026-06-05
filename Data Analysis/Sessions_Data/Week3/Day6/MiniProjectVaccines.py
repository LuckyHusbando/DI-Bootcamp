#Mini-Project Vaccines

# Part 1

class Human:
    """
    Represents a citizen of the city.
    """
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

class Queue:
    """
    Represents a queue of humans waiting for their vaccine.
    """
    def __init__(self):
        self.humans = []

    def add_person(self, person: Human):
        if person.age > 60 or person.priority:
            new_list = [person]
            for h in self.humans:
                new_list.append(h)
            self.humans = new_list
        else:
            self.humans.append(person)

    def find_in_queue(self, person: Human):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return None

    def swap(self, person1: Human, person2: Human):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 is not None and index2 is not None:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if not self.humans:
            return None
        
        next_person = self.humans[0]
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type: str):
        if not self.humans:
            return None
            
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                next_person = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return next_person
        return None

    def sort_by_age(self):
        # Using a bubble sort-like approach to avoid forbidden methods
        n = len(self.humans)
        for i in range(n):
            for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
                # In this case, we define "greater" by our sorting logic
                
                # Priority people should always come first
                if self.humans[j].priority and not self.humans[j+1].priority:
                    self.swap(self.humans[j], self.humans[j+1])
                    continue
                
                # Older people should come before younger people
                if not self.humans[j].priority and not self.humans[j+1].priority:
                    if self.humans[j].age < self.humans[j+1].age:
                        self.swap(self.humans[j], self.humans[j+1])

# Part 2

class Human(Human):
    """
    Extending the Human class for Part 2.
    """
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        super().__init__(id_number, name, age, priority, blood_type)
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

class Queue(Queue):
    """
    Extending the Queue class for Part 2.
    """
    def rearrange_queue(self):
        if len(self.humans) < 2:
            return

        i = 0
        while i < len(self.humans) - 1:
            person1 = self.humans[i]
            person2 = self.humans[i+1]
            
            if person2 in person1.family:
                # Find a person to swap with person2 who is not in person1's family
                found_swap = False
                for j in range(i + 2, len(self.humans)):
                    person_to_swap = self.humans[j]
                    if person_to_swap not in person1.family:
                        self.swap(person2, person_to_swap)
                        found_swap = True
                        break
                
                if not found_swap:
                    # If no one can be swapped, move the queue element to the end
                    # This is one way to handle it without modifying the original order much
                    self.humans.append(self.humans.pop(i + 1))
                    
            i += 1
