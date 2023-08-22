from codrone_edu.drone import Drone

def flight_check():
    print("Creating drone object")
    drone = Drone()
    print("Getting ready to pair")
    drone.pair()
    print("Paired!")
    drone.close()

if __name__ == "__main__":
    flight_check()

