from queue import PriorityQueue

class Agente:
    def __init__(self, initial_state, goal_state):
        # Initializing the agent with the initial and goal states
        self.initial_state = initial_state
        self.goal_state = goal_state

    def heuristic(self, puzzle):
        # Computing the heuristic using Hamming distance
        # hamming code = number of bits of the current state different from the goal state
        return sum([1 if puzzle[i] != self.goal_state[i] else 0 for i in range(9)])

    def actions(self, puzzle):
        # Determining the possible actions based on the blank tile position
        possible_actions = []
        blank = puzzle.index(0)
        if blank % 3 != 0: possible_actions.append('Left')
        if blank % 3 != 2: possible_actions.append('Right')
        if blank // 3 != 0: possible_actions.append('Up')
        if blank // 3 != 2: possible_actions.append('Down')
        return possible_actions

    def transition(self, puzzle, action):
        # Applying an action to the puzzle and returning the new state
        new_puzzle = puzzle[:]
        blank = puzzle.index(0)
        if action == 'Left':  new_puzzle[blank], new_puzzle[blank-1] = new_puzzle[blank-1], new_puzzle[blank]
        if action == 'Right': new_puzzle[blank], new_puzzle[blank+1] = new_puzzle[blank+1], new_puzzle[blank]
        if action == 'Up':    new_puzzle[blank], new_puzzle[blank-3] = new_puzzle[blank-3], new_puzzle[blank]
        if action == 'Down':  new_puzzle[blank], new_puzzle[blank+3] = new_puzzle[blank+3], new_puzzle[blank]
        return new_puzzle

    def solve(self):
        # Implementing the A* search algorithm to find the solution
        frontier = PriorityQueue() # Priority queue for the frontier
        frontier.put((0, self.initial_state))
        # notebook where the trace of where you came from and what action you took to reach this new path was noted
        came_from = {tuple(self.initial_state): None}
        # notebook where the information on the paths/costs of where you have already passed is recorded:
        cost_so_far = {tuple(self.initial_state): 0} # Keeping track of the cost

        while not frontier.empty():
            _, current = frontier.get()
            if current == self.goal_state:
                # Reconstructing the path if the goal is reached ([0,1,2,3,4,5,6,7,8])....
                # if it's not reached go to the "for"
                path = []
                while current != self.initial_state:
                    previous = came_from[tuple(current)]
                    path.append((current, previous[1]))
                    current = previous[0]
                path.reverse()
                return path


            # For every possible action in the current state, we explore the neighbor
            for action in self.actions(current):
                # New state after the action
                new_puzzle = self.transition(current, action)
                # And the new cost
                new_cost = cost_so_far[tuple(current)] + 1

                # If the new state is really new or has a lower cost, we update the dictionaries
                if tuple(new_puzzle) not in cost_so_far or new_cost < cost_so_far[tuple(new_puzzle)]:
                    # If it's a new or easier path, we update our "notebook" with the new cost.
                    cost_so_far[tuple(new_puzzle)] = new_cost
                    # It calculates a "priority" for this path,
                    # which is the cost + an estimate of how far it is from the end.
                    # It's like a tip on which paths to try first.
                    priority = new_cost + self.heuristic(new_puzzle)
                    # We put this new path in a list of paths to be explored,
                    # sorted by "priority".
                    # It's like you're queuing up the most promising paths to try first.
                    frontier.put((priority, new_puzzle))
                    # Write down where you came from and what action you took to reach this new path.
                    # It's like you're drawing a map of the maze as you explore.
                    came_from[tuple(new_puzzle)] = (current, action)

        # If the frontier is empty and we haven't found a solution, we return None
        return None
