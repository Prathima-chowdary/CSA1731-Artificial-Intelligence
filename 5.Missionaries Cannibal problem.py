from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.boat == 'left' and self.missionaries < self.cannibals:
            return False
        if self.boat == 'right' and self.missionaries > self.cannibals:
            return False
        return True

    def next_states(self):
        next_states = []
        for missionaries in range(-2, 3):
            for cannibals in range(-2, 3):
                if missionaries == 0 and cannibals == 0:
                    continue
                new_boat = 'left' if self.boat == 'right' else 'right'
                new_state = State(
                    self.missionaries + missionaries,
                    self.cannibals + cannibals,
                    new_boat
                )
                if new_state.is_valid():
                    next_states.append(new_state)
        return next_states

def solve_missionaries_and_cannibals():
    initial_state = State(3, 3, 'left')
    visited = set()
    queue = deque([initial_state])
    while queue:
        current_state = queue.popleft()
        if current_state.missionaries == 0 and current_state.cannibals == 0:
            return current_state
        visited.add(current_state)
        for next_state in current_state.next_states():
            if next_state not in visited:
                queue.append(next_state)
    return None

if __name__ == '__main__':
    solution = solve_missionaries_and_cannibals()
    if solution is None:
        print("No solution found")
    else:
        print("Solution:")
        print("Missionaries left:", solution.missionaries)
        print("Cannibals left:", solution.cannibals)
        print("Boat position:", solution.boat)
