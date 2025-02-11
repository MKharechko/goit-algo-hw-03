import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    
    if min >= max or quantity > (max - min + 1) or quantity <= 0:
        return []
    
    if min < 1:
        return []
    if max > 1000:
        return []    

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


numbers = get_numbers_ticket(1, 99, 4) 
print("Ваші унікальні лотерейні числа:", numbers)
