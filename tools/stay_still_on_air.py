from codrone_edu.drone import Drone
from pre_flight_check import flight_check
from buzz_alert import buzzer
from time import sleep


def onair():
    drone = Drone()
    drone.pair()
    print("Paired!")
    drone.takeoff()
    sleep(2)
    print("In the air!")


if __name__ == "__main__":
    flight_check()
    buzzer()
    flynow()
