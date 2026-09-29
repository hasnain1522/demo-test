"""Small demo application with intentional engineering problems."""


def calculate_total(price, quantity, discount, tax, shipping, loyalty, coupon):
    # TODO: validate inputs and separate pricing rules.
    subtotal = price * quantity
    subtotal = subtotal - discount
    subtotal = subtotal + tax
    subtotal = subtotal + shipping
    subtotal = subtotal - loyalty
    if coupon:
        subtotal -= 5
    return subtotal


def greet_user(name):
    """Return a greeting for a user."""
    # FIXME: handle blank names consistently.
    return "Hello, " + name


if __name__ == "__main__":
    print(greet_user("Demo User"))
    print(calculate_total(100, 2, 10, 5, 8, 3, True))
