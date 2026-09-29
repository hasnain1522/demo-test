import math


def calculate_circle(radius):
    return math.pi * radius * radius


def unused_helper(value):
    return value * 2


def format_result(value):
    return f"Result: {value}"


def run():
    radius = 5
    value = calculate_circle(radius)
    print(format_result(value))


if __name__ == "__main__":
    run()
