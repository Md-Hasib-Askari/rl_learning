from pynput import keyboard

# 2. Create a manual grid-world agent:
grid = [['S', ' ', 'G'],
        [' ', 'X', ' '],
        [' ', ' ', ' ']]
# S = Start, G = Goal (+10 reward), X = Obstacle (-5 reward)
# Actions: Up, Down, Left, Right (manual control using arrow keys)

def print_grid():
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) == position:
                print("A", end=" ")  # Print agent position
            else:
                if col == ' ':
                    print('.', end=" ")  # Empty space
                else:
                    print(col, end=" ")
        print()

# track total reward per episode
total_reward = 0
position = (0, 0)  # Starting position at 'S'
def move_agent(action):
    global position, total_reward
    x, y = position
    if action == 'UP' and x > 0:
        x -= 1
    elif action == 'DOWN' and x < 2:
        x += 1
    elif action == 'LEFT' and y > 0:
        y -= 1
    elif action == 'RIGHT' and y < 2:
        y += 1

    if grid[x][y] == 'X':
        total_reward -= 5
    elif grid[x][y] == 'G':
        total_reward += 10
        print("Goal reached! Total reward:", total_reward)
        position = (x, y)

        print_grid()
        return True  # Episode ends
    
    position = (x, y)
    return False  # Episode continues

# Example of moving the agent
done = False
while not done:
    print_grid()

    print("Use arrow keys to move (or 'q' to quit).")
    action = None

    def on_press(key):
        global action
        try:
            if key == keyboard.Key.up:
                action = 'UP'
            elif key == keyboard.Key.down:
                action = 'DOWN'
            elif key == keyboard.Key.left:
                action = 'LEFT'
            elif key == keyboard.Key.right:
                action = 'RIGHT'
            elif hasattr(key, 'char') and key.char == 'q':
                action = 'QUIT'
        except AttributeError:
            pass
        # return False to stop the listener once we have an action
        if action is not None:
            return False
        return None

    with keyboard.Listener(on_press=on_press) as listener: # type: ignore
        listener.join()

    if action == 'QUIT':
        print("Quitting.")
        done = True
        continue
    done = move_agent(action)
    print("Current position:", position, "Total reward:", total_reward)
