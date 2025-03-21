import re

phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)

    if cleaned_number.startswith("380"):
        return "+" + cleaned_number
    elif cleaned_number.startswith("0"):  
        return "+38" + cleaned_number
    else:
        return "+38" + cleaned_number


normalized_numbers = [normalize_phone(phone.strip()) for phone in phone_number]
for original, normalized in zip(phone_number, normalized_numbers):
    print(f"Оригінальний: {original.strip()} → Нормальний: {normalized}")