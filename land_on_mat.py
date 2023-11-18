import keyboard
from djitellopy import Tello

# Create a Tello object and establish a connection
tello = Tello()
tello.connect()

# Retrieve and display the battery percentage
battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")

tello.takeoff()
tello.set_speed(20)
tello.move_up(100)

# Continuously check for the 'esc' key press to exit the loop
while not keyboard.is_pressed('esc'):
    # Get the distance to an obstacle (mat) under the drone
    dist = tello.get_distance_tof()

    if dist < 50:
        # Land on a obstacle (mat) if the distance is less than 50 cm
        break
    else:
        # Move slowly downward
        tello.move_down(20)

tello.land()
