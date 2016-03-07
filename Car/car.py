max_speed = 100
car_speed = 0
car_doors = False

def open_doors():
    global car_doors, car_speed
    car_doors = True
    if car_speed>0:
        car_speed = 0
        print("Car was stopped and doors opened")
    print("Car doors were opened")
def close_doors():
    global car_doors
    car_doors = False
    print("Car doors were closed")

def accelerate(amount_to_accelerate):
    global car_doors, car_speed
    if not car_doors:
        car_speed += amount_to_accelerate
    else:
        print("Car doors open, can't accelerate")
    if car_speed > max_speed:
        car_speed = max_speed
def current_state():
    global car_doors, car_speed
    if car_doors:
        print("Car doors are open and car is stopped")
    else:
        print("Car is driving with a speed of {0}".format(car_speed))
def car_stop():
    global car_speed
    car_speed = 0


def main():
    current_state()
    accelerate(20)
    current_state()
    open_doors()
    close_doors()
    accelerate(30)
    current_state()
    close_doors()
    car_stop()
    current_state()

if __name__ == "__main__":
    main()