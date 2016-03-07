from Rectangle import Rectangle

if __name__ == "__main__":
    rect = Rectangle(50,50)
    rect_two = Rectangle(50,50)

    print("Area of rect: ",rect.get_area())
    print("Is rect equal to rect_two ? ",rect.equal_to(rect_two))