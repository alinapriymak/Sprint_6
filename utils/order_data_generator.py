import random


def generate_name():
    names = ["Александр", "Дмитрий", "Максим", "Иван", "Сергей", "Анна", "Екатерина", "Мария", "Ольга", "Татьяна"]
    return random.choice(names)


def generate_surname():
    surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Козлова", "Морозова", "Новикова", "Волкова", "Соколова"]
    return random.choice(surnames)


def generate_address():
    streets = ["Ленина", "Мира", "Гагарина", "Пушкина", "Садовая", "Цветной бульвар", "Тверская", "Арбат"]
    numbers = random.randint(1, 150)
    return f"ул. {random.choice(streets)}, д. {numbers}"


def generate_metro_station():
    stations = [
        "Сокольники",
        "Черкизовская",
        "Преображенская площадь",
        "Комсомольская",
        "Киевская",
        "Курская",
        "Белорусская"
    ]
    return random.choice(stations)


def generate_phone():
    return f"+79{random.randint(100000000, 999999999)}"


def generate_rental_days():
    days = ["сутки", "двое суток", "трое суток", "четверо суток", "пятеро суток", "шестеро суток", "семеро суток"]
    return random.choice(days)


def generate_color():
    return random.choice(["black", "grey"])


def generate_comment():
    comments = [
        "Позвонить за час",
        "Домофон 123",
        "Оставить у двери",
        "Без комментариев",
        "Срочно!",
        "Оплата картой",
        ""
    ]
    return random.choice(comments)


def generate_order_data():
    """Генерация случайного набора данных для заказа"""
    return {
        "name": generate_name(),
        "surname": generate_surname(),
        "address": generate_address(),
        "metro_station": generate_metro_station(),
        "phone": generate_phone(),
        "rental_days": generate_rental_days(),
        "color": generate_color(),
        "comment": generate_comment(),
    }