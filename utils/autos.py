class Car:

    def __init__(self):
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False

    def start_engine(self):
        if self.__engine_running:
            raise ValueError("Engine is already running!")
        else:
            self.__engine_running = True
            print("Engine is running!")

    def stop_engine(self):
        if not self.__engine_running:
            raise ValueError("Engine is already stopped!")
        else:
            self.__engine_running = True
            print("Engine stopped!")

    def can_drive(self, km):
        _range = self.__gas_in_tank / self.get_consumption()
        if km > _range:
            return False
        return True

    def drive(self, km):
        if not self.__engine_running:
            raise ValueError("Engine is not running!")
        if not self.can_drive(km):
            raise ValueError("Not enough gas!")
        self.__gas_in_tank -= self.get_consumption() * km
        print(f"You have arrived at your destination! You used {self.get_consumption() * km} litters of gas!")

    def get_consumption(self):
        return self.__cmc / 100000 * 4 + (0.5 * len(self.__passengers))

    def refill(self, litters):
        if litters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank += litters

    def get_doors(self):
        return self.__doors
    
    def get_gas_percentage(self):
        return self.__gas_in_tank / self.__tank_capacity * 100
    
    def add_person(self, person):
        if len(self.__passengers) == self.get_doors():
            raise ValueError("Too many passagers!")
        self.__passengers.append(person)

class GasStation:

    def __init__(self, pin):
        self.__price = 0
        self.__busy = False
        self.__pin = pin

    def is_busy(self):
        return self.__busy

    def get_price(self):
        return self.__price
    
    def set_price(self, price, pin):
        if pin != self.__pin:
            raise ValueError("Wrong pin")
        self.__price = price
    
    def fill(self, car: Car, litters: int):
        if self.__busy:
            raise ValueError("Busy")
        car.stop_engine()
        self.__busy = True
        for x in range(1, litters + 1):
            try:
                car.refill(1)
            except ValueError:
                break
        self.__busy = False
        return x * self.__price
        