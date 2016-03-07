def fahrenheit_to_kelvin(temp):
    # Formula: T(K) = (T(°F) + 459.67) × 5/9
    answer = (temp + 459.67) * (5/9)
    return answer


def celsius_to_fahrenheit(celsius):
    # Formula: T(°F) = T(°C) × 9/5 + 32
    answer = (celsius * 9/5) + 32
    return answer


def are_you_an_adult():
    age = input('What is your age: ')
    return int(age) >= 18


if __name__ == "__main__":
    print(fahrenheit_to_kelvin(0), 'K' )
    print(celsius_to_fahrenheit(10), 'F')
    print(are_you_an_adult())