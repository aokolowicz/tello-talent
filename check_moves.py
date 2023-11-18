from djitellopy import Tello

# Create a Tello object and establish a connection
tello = Tello()
tello.connect()

# Retrieve and display the battery percentage
battery_level = tello.get_battery()
print(f"Battery Percentage: {battery_level}")

tello.takeoff()

# Draw the 1st rectangle
tello.move_left(30)
tello.move_up(30)
tello.move_right(60)
tello.move_down(30)
tello.move_left(30)

# Draw the 2nd rectangle
tello.move_back(30)
tello.move_up(30)
tello.move_forward(60)
tello.move_down(30)
tello.move_back(30)

tello.land()
