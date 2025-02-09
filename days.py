from datetime import datetime

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, "%Y.%m.%d").date()
        current_date = datetime.today().date()
        delta_days = (user_date - current_date).days
        return delta_days
    except ValueError:
        return "Невірний формат дати. Використовуйте YYYY.MM.DD."
print(get_days_from_today("2025.06.09"))
    