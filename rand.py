import random

def get_numbers_ticket(min_value, max_value, quantity):
    return random.sample(range(min_value, max_value + 1), quantity)

lottery_numbers = get_numbers_ticket(1, 99, 4)
print("Ваші унікальні лотерейні числа:", lottery_numbers)