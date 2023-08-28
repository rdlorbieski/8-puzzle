import pygame
import random
from time import sleep
from agente import Agente
from copy import deepcopy

# Constants
WIDTH, HEIGHT = 300, 350
TILE_SIZE = WIDTH // 3
FONT_SIZE = 20
BUTTON_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Puzzle Solver")
font = pygame.font.Font(None, FONT_SIZE)

#The 8-puzzle has an interesting property: not all initial states are solvable. To determine if a state is solvable,
# you can calculate the "inversion".
def is_solvable(state):
    inversions = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions % 2 == 0

# Generate a random initial state
def generate_initial_state():
    state = list(range(9))
    while True:
        random.shuffle(state)
        if is_solvable(state):
            return state

# Draw the board
def draw_board(state):
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            color = WHITE if tile == 0 else GRAY
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
            if tile != 0:
                text = font.render(str(tile), True, BLACK)
                screen.blit(text, (j * TILE_SIZE + TILE_SIZE // 3, i * TILE_SIZE + TILE_SIZE // 3))


# Draw the start and reset buttons
def draw_buttons():
    pygame.draw.rect(screen, GRAY, (0, WIDTH, WIDTH // 2, BUTTON_HEIGHT))
    start_text = font.render("Start AI", True, BLACK)
    screen.blit(start_text, (WIDTH // 6, WIDTH + BUTTON_HEIGHT // 3))
    pygame.draw.rect(screen, GRAY, (WIDTH // 2, WIDTH, WIDTH // 2, BUTTON_HEIGHT))
    reset_text = font.render("Reset", True, BLACK)
    screen.blit(reset_text, (2 * WIDTH // 3, WIDTH + BUTTON_HEIGHT // 3))

def main():
    initial_state = generate_initial_state()
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    agent = Agente(deepcopy(initial_state), goal_state) # Pass a copy of the initial state
    running = True
    started = False

    while running:
        screen.fill(WHITE)
        draw_board(initial_state)
        draw_buttons()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y > WIDTH and y < WIDTH + BUTTON_HEIGHT:
                    if x < WIDTH // 2 and not started:  # Clicked on the "Start AI" button
                        started = True
                        path = agent.solve()
                        if path is not None:
                            for step in path:
                                state, _ = step
                                initial_state = state
                                draw_board(initial_state)
                                pygame.display.flip()
                                sleep(0.7)
                    elif x >= WIDTH // 2:  # Clicked on the "Reset" button
                        initial_state = generate_initial_state() # Regenerate initial_state
                        agent = Agente(deepcopy(initial_state), goal_state) # Create a new agent with the new initial state
                        started = False

    pygame.quit()

if __name__ == "__main__":
    main()