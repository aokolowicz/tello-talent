import keyboard
from djitellopy import Tello

# Create a Tello object and establish a connection
tello = Tello()
tello.connect()

# Create a dictionary to map keys to actions
key_actions = {
    'up': lambda tello: (
        tello.send_expansion_command('mled s p O'),
        tello.move_forward(30),
    ),
    'down': lambda tello: (
        tello.send_expansion_command('mled s p X'),
        tello.move_back(30),
    ),
    'left': lambda tello: (
        tello.send_expansion_command('mled r p 2.5 >>>'),
        tello.move_left(30),
    ),
    'right': lambda tello: (
        tello.send_expansion_command('mled l p 2.5 <<<'),
        tello.move_right(30),
    ),
    'w': lambda tello: (
        tello.send_expansion_command('mled u p 2.5 ^^^'),
        tello.move_up(20),
    ),
    's': lambda tello: (
        tello.send_expansion_command('mled d p 2.5 vvv'),
        tello.move_down(20),
    ),
    'a': lambda tello: (
        tello.send_expansion_command('mled s b >'),
        tello.rotate_counter_clockwise(45),
    ),
    'd': lambda tello: (
        tello.send_expansion_command('mled s b <'),
        tello.rotate_clockwise(45),
    ),
}

# Retrieve and display the battery percentage
battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")

tello.takeoff()

while True:
    if keyboard.is_pressed('esc'):
        break

    # Check for key presses corresponding to defined actions
    for key in key_actions:
        if keyboard.is_pressed(key):
            # Execute the corresponding action
            key_actions[key](tello)
            tello.send_expansion_command("mled sc")
        if keyboard.is_pressed('esc'):
            break

tello.land()
