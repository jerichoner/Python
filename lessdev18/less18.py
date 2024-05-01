# Импортируем необходимый модуль для измерения времени
import time

# Первое задание: программа для арифметических операций и обработка исключения деления на ноль
def perform_operation(x, y, operation):
    try:
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            if y == 0:
                raise ZeroDivisionError("Ошибка: Деление на ноль не возможно")
            return x / y
    except ZeroDivisionError as e:
        print(e)

# Второе задание: создание пользовательского исключения ValidationError
class ValidationError(Exception):
    pass

def validate_username(username):
    if not username or not username.isalnum():
        raise ValidationError("Некорректное имя пользователя. Должно быть непустым и содержать только буквы и цифры.")

# Третье задание: контекстный менеджер для измерения времени выполнения блока кода
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = (self.end - self.start) * 1000

# Пример использования
# Первое задание
print(perform_operation(10, 5, 'add'))          # 15
print(perform_operation(10, 0, 'divide'))       # Ошибка: Деление на ноль не возможно

# Второе задание
try:
    validate_username("User@name")
except ValidationError as e:
    print(e)                                     # Некорректное имя пользователя...

# Третье задание
with Timer() as t:
    # Предположим, что здесь пользователь вводит данные и программа их обрабатывает
    time.sleep(1)  # Имитация задержки в 1 секунду

print(f"Время выполнения блока кода: {t.interval:.2f} миллисекунд.")  # Вывод времени выполнения
