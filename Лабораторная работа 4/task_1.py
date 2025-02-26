class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"Авто: {self.brand} {self.model}, {self.year}"

    def __repr__(self) -> str:
        return f"Vehicle({self.brand}, {self.model}, {self.year})"


class Car(Vehicle):
    """Дочерний класс для легковых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, seats: int) -> None:
        super().__init__(brand, model, year)
        self.seats = seats

    def __str__(self) -> str:
        return f"Легковая: {self.brand} {self.model}, {self.year}, {self.seats} мест"


class Truck(Vehicle):
    """Дочерний класс для грузовых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, max_load: float) -> None:
        super().__init__(brand, model, year)
        self.max_load = max_load

    def __str__(self) -> str:
        return f"Грузовик: {self.brand} {self.model}, {self.year}, {self.max_load} т"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 5)
    truck = Truck("Volvo", "FH16", 2020, 20.0)

    print(car)
    print(truck)