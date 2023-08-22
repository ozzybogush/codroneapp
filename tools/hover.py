from codrone_edu.drone import *


def hover():
    drone = Drone()
    drone.pair()
    drone.takeoff()
    drone.hover(3)
    drone.land()
    drone.close()


if __name__ == "__main__":
    hover()
