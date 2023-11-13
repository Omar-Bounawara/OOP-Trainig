"""
Priority Queue Implementation

Author: Omar-Bounawara

Description:
This Python script implements a priority queue class ('pq') that manages a collection of elements with associated priorities. The script provides methods for inserting elements, popping elements, and sorting the queue based on priorities.

Usage:
- Initialize the priority queue with a list of elements and priorities.
- Insert new elements into the queue with specified priorities.
- Pop elements from the queue, optionally specifying the number of elements to pop.
- Sort the queue based on priorities.

Note: This script uses a list of dictionaries to represent elements with associated priorities.

Constraints:
- The script assumes that the input priorities are integers between 0 and 10.
- The priorities are randomly generated for demonstration purposes.


"""



import random
class pq():
    def __init__(self, list_of_elements):
        self.queue = list_of_elements
        self.size = len(list_of_elements)


    def __repr__(self):
        str=""
        for x in self.queue:
            str+=(f'priority: {x.get("priority")}, element: {x.get("element")}\n')
        return str[:-1]





    def __iter__(self):
        self.pos=0
        return self

    def __next__(self):
        if self.pos < len(self.queue):
            x = self.pos
            self.pos += 1
            return self.queue[x]
        else:
            raise StopIteration


    def sort_queue(self):

        self.queue = sorted(self.queue, key=lambda x: x.get("priority"))

    def insert(self, element, priority):
        self.queue.append({"element": element, "priority": priority})
        self.sort_queue()  # Sort the queue after insertion
        self.size+=1

    def pop(self, number=1):
        for i in range(number):
            self.queue.pop()
            self.size -= 1



# Generate a large list of elements with random priorities
elements = [{"element": f"task{i}", "priority": random.randint(0, 10)} for i in range(100)]

# Create a priority queue
large_queue = pq(elements)

#initial queue
print("Initial Large Queue:")
print(large_queue)

# Insert a new task with priority 50
large_queue.insert("new_task", 50)
print("\nLarge Queue after insertion:")
print(large_queue)

# Pop three elements from queue
large_queue.pop(3)
print("\nLarge Queue after popping 3 elements:")
print(large_queue)

# Sort the queue
large_queue.sort_queue()
print("\nLarge Queue after sorting:")
print(large_queue)
