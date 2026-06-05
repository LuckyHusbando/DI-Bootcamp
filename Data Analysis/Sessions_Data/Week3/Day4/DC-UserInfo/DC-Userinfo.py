#DC - User Info Challenge (Day 4, Week 3)

def main():
    """
    Asks the user for five sets of name, age, and score inputs,
    creates a list of tuples, and sorts it by name, then age, then score.
    """
    data = []
    for _ in range(5):
        name = input("Enter name: ")
        age = input("Enter age: ")
        score = input("Enter score: ")
        data.append((name, age, score))

    # The lambda function sorts by three criteria: name, then age, then score.
    # The `key` parameter in sorted() specifies a function to be called on
    # each element prior to making comparisons. Here, it's a lambda function
    # that returns a tuple of the element's name, age, and score. Python's
    # default tuple comparison handles the multi-level sorting.
    sorted_data = sorted(data, key=lambda item: (item[0], item[1], item[2]))
    
    print("\nOriginal list of tuples:")
    print(data)
    
    print("\nSorted list of tuples:")
    print(sorted_data)

if __name__ == "__main__":
    main()

