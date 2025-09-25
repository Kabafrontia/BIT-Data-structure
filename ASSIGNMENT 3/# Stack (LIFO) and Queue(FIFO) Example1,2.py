# Stack (LIFO) Example
stack = []

# Practical (Rwanda): Irembo
stack = ["Fill Form", "Upload File", "Submit"]
stack.pop()   # Undo one
print("Irembo remains:", stack)

# Practical (Rwanda): UR
stack = ["Rev1", "Rev2", "Rev3"]
while stack:
    stack.pop()
print("UR remains:", stack)  


# Queue (FIFO) Example
from collections import deque

# Practical (Rwanda): CHUK
queue = deque(["P1", "P2", "P3", "P4"])
queue.popleft()  # serve P1
queue.popleft()  # serve P2
print("CHUK front patient:", queue[0])

# Practical (Rwanda): Airtel
queue = deque(["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"])
print("Airtel last client:", queue[-1])  