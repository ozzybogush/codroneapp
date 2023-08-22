from codrone_edu.drone import *
import time


def trim():
    drone = Drone()
    drone.pair()
    drone.set_trim(-5, 0)  # Example: Assume the drone flows to the right, and trim slightly to the left.
    time.sleep(1)  # Add time.sleep(1) before takeoff() if you want to trim before takeoff.
    drone.takeoff()
    drone.hover(3)
    drone.land()
    drone.close()
