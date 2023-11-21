def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_temperature(temperature, scale):
    if scale.upper() == 'C':
        return (temperature - 32) * 5.0/9.0
    elif scale.upper() == 'F':
        return temperature * 9.0/5.0 + 32

def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12.0
    number_of_payments = years * 12
    monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments))
    return monthly_payment

def is_palindrome_number(number):
    return str(number) == str(number)[::-1]
