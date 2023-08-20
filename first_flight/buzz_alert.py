from time import sleep
from codrone_edu.drone import Drone, Note

def buzzer():
    drone = Drone()
    drone.pair()
    drone.set_drone_LED(255, 255, 255, 255)
    drone.drone_buzzer(Note.C4, 1000)
    drone.drone_buzzer(Note.D4, 1000)
    drone.drone_buzzer(Note.E4, 1000)
    drone.close()

if __name__ == "__main__":
    buzzer()
