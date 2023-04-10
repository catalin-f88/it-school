class Employee:
    def __init__(self, first_name, last_name, email, gross_salary) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gross_salary = gross_salary
        self.__ssm_signed = False
    
    def sign_ssm(self):
        self.__ssm_signed = True

    def sign_presence(self):
        pass

    def get_net_salary(self):
        return self.__gross_salary

    def pay(self):
        print(f"Amount to transfer: {self.get_net_salary()}")

class FullTimeEmployee(Employee):
    pass


class Contractor(Employee):
    pass


class NoTaxEmployee(Employee):
    pass


class PartTimeEmployee(Employee):
    def pay(self):
        super().pay()


employees = [
    FullTimeEmployee("Marcel", "Ionescu", "marcelionescu@gmail.com", 4500),
    Contractor("Mihai", "Dinescu", "mdinescu@gmail.com", 8000),
    PartTimeEmployee("Ionut", "Iancu", "iiancu@gmail.com", 3000),
    NoTaxEmployee("George", "Grigore", "ggrigore@gmail.com", 6000),
    ]