
# 8-Puzzle Solver

The 8-Puzzle Solver is a Python application that solves the classic 8-puzzle game using artificial intelligence. The solution is visualized using a graphical user interface (GUI) built with Pygame, allowing the user to interact with the solver, start the AI, and reset the puzzle.


## Features

- **Graphical User Interface:** Provides a visual representation of the 8-puzzle board, with numbered tiles and blank space.
- **Random Initial State:** Generates a random solvable initial state for the 8-puzzle.
- **AI Solver:** Utilizes computational agents and the A* search algorithm to find the optimal solution to the puzzle.
- **Start AI Button:** Allows the user to start the AI to solve the puzzle.
- **Reset Button:** Allows the user to reset the puzzle to a new random initial state.
- **Step-by-Step Visualization:** Displays each step of the solution with a 0.7-second delay, allowing the user to follow the solving process.

## How to Use

- **Start the Application:** Run the main.py file to launch the application.
- **View the Initial State:** Observe the randomly generated initial state of the 8-puzzle.
- **Start the AI:** Click the "Start AI" button to initiate the solving process. The AI will solve the puzzle, and each step will be displayed on the board.
- **Reset the Puzzle:** Click the "Reset" button to generate a new random initial state and reset the puzzle.
- **Exit the Application:** Close the window to exit the application.

## How to Use

- **Start the Application:** Run the main.py file to launch the application.
- **View the Initial State:** Observe the randomly generated initial state of the 8-puzzle.
- **Start the AI:** Click the "Start AI" button to initiate the solving process. The AI will solve the puzzle, and each step will be displayed on the board.
- **Reset the Puzzle:** Click the "Reset" button to generate a new random initial state and reset the puzzle.
- **Exit the Application:** Close the window to exit the application.

## Code Structure


- **main.py:** Contains the main application logic, including the Pygame loop and GUI functions.

- **agente.py:** Contains the AI agent class, responsible for solving the 8-puzzle using a heuristic approach.
## Challenges


Implementing the 8-puzzle using computational agents and the A* search algorithm presents several challenges:

1. **State Space Size and Memory Usage**: 
    - The 8-puzzle has \(9!\) (362,880) possible states, but only half of these are solvable. This large state space can make the A* search computationally expensive, especially if the heuristic used is not admissible or not informative enough.

2. **Choice of Heuristic**:
    - The efficiency of A* largely depends on the heuristic used. Common heuristics for the 8-puzzle include the Manhattan distance and the number of misplaced tiles. An ideal heuristic is both admissible (never overestimates the cost to reach the goal) and informative (provides a good estimate of the actual cost).

3. **Finding an Optimal Solution**:
    - A* guarantees an optimal solution if an admissible heuristic is used. However, the search can take a long time if the initial state is far from the goal state, or if there are many states with the same heuristic value.

4. **Checking Solvability**:
    - Not all 8-puzzle states are solvable. Before starting the search, the algorithm should check if the given state is solvable, or it may search indefinitely.

5. **Action Generation and State Transition**:
    - The computational agents must be able to generate valid actions for a given state (e.g., you can't move left if the blank tile is on the left edge) and apply these actions to produce new states.

6. **Avoiding Repeated States**:
    - To improve efficiency, the algorithm should avoid revisiting states it has already explored. This requires efficient data structures to store and check previously visited states.

7. **Real-time Interaction**:
    - If integrating with a GUI, the algorithm should provide real-time feedback or be able to run in the background without freezing the interface.

8. **Termination**:
    - The algorithm should be able to terminate gracefully if it becomes clear that a solution cannot be found in a reasonable time, or if the puzzle is unsolvable.

9. **Generalizing the Solution**:
    - While the 8-puzzle has a fixed size, there are variations like the 15-puzzle. The implementation should ideally be flexible enough to handle different sizes without significant modifications.

Addressing these challenges requires a combination of algorithmic knowledge, data structures, heuristics, and efficient coding practices. The reward, however, is a robust solution that can solve the 8-puzzle quickly and optimally.


## Prerequisites

- Python 3.x: Ensure you have Python 3.x installed. If not, download and install it from the [official website](https://www.python.org/downloads/).
- pip: Ensure you have the pip package installer for Python. It is usually included with the Python installation.

## 8-Puzzle Solver: Installation Guide


1. **Clone the Repository**:

2. **Install Required Python Libraries**:
   Using pip, install the required libraries. The primary dependency is `pygame`.
   ```bash
   pip install pygame
   ```

3. **Run the Application**:
   Navigate to the directory containing the `main.py` file and run:
   ```bash
   python main.py
   ```
   This will launch the 8-Puzzle Solver application. Follow the on-screen instructions to interact with the application.
## Demonstration of Results

![Logo](https://rodolfo.lorbieski.eti.br/portfolio/8_puzzle.gif)


## Autores

- [@rdlorbieski](https://github.com/rdlorbieski)
