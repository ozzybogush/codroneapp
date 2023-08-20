from codrone_edu.drone import Drone
from pre_flight_check import flight_check
from buzz_alert import buzzer
from time import sleep
def flynow():
    drone = Drone()
    drone.pair()
    print("Paired!")
    drone.takeoff()
    print("Performing flip!")
    drone.flip(direction="front")
    sleep(2)
    print("In the air!")
    print("Landing")
    drone.land()
    drone.close()
    print("Program complete")

if __name__ == "__main__":
    flight_check()
    buzzer()
    flynow()
