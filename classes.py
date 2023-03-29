from utils import autos
from utils import users


gas1 = autos.GasStation(1234)
gas1.set_price(6.55, 1234)
# print(gas1.get_price())

vw = autos.Car()

print(vw.get_gas_percentage())
print(f"Aveti de plata: {gas1.fill(vw, 10)}")
print(vw.get_gas_percentage())

catalin = users.Person()
mihai = users.Person()

# vw.start_engine()
# vw.refill(10)
# vw.drive(200)
# print(vw.get_consumption())
vw.add_person(catalin)
vw.add_person(mihai)
# print(f"Fuel remaining {vw.get_gas_percentage():.2f} %")
# vw.stop_engine()

# print(vw.get_consumption())


# catalin = users.Person()
# print(f"Inaltime in CM: {catalin.get_cm_height()}")
# print(f"Inaltime in M: {catalin.get_m_height()}")