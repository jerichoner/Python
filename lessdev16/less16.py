class Vehicle():
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Модель {self.model}; Год выпуска - {self.year}")

class Car(Vehicle):
    def __init__(self, model, year, fuel_type):
        super().__init__(model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Тип топлива - {self.fuel_type}")

class Toyota(Car):
    def __init__(self, model, year, fuel_type, model_name):
        super().__init__(model, year, fuel_type)
        self.model_name = model_name

    def display_info(self):
        super().display_info()
        print(f"Название модели - {self.model_name}")

class Zeekr(Car):
    def __init__(self, model, year, fuel_type, fuel_efficiency, model_name):
        super().__init__(model, year, fuel_type)
        self.fuel_efficiency = fuel_efficiency
        self.model_name = model_name

    def display_info(self):
        super().display_info()
        print(f"Эффективность использования топлива - {self.fuel_efficiency}\nНазвание модели - {self.model_name}")

toyota = Toyota("Toyota", 2022, "Бензин", "Camry")
zeekr = Zeekr("Zeekr", 2023, "Электричество", "Экономия энергии", "001")

toyota.display_info()
print("=============================================================================")
zeekr.display_info()
