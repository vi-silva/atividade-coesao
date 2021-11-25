#'Tesla Model 3':
#445000
#'Chevrolet Bold':
#317000
#'BMW i3':
#319950
#'Honda Civic LX':
#127900

import string
import random

class Vehicle:
    model = str
    catalogue_price = int
    is_electric = bool
    id = str
    license_plate = str
    tax_percentage = float

    def __init__ (self, model, catalogue_price, is_electric):
        self.model = model
        self.catalogue_price = catalogue_price
        self.is_electric = is_electric
        self.id = VehicleRegistry.generate_vehicle_id(12)
        self.license_plate = VehicleRegistry.generate_vehicle_license(self.id)
        self.tax_percentage = TaxPercentage.tax_percentage(self)

class VehicleRegistry:
    @staticmethod
    def generate_vehicle_id(length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"

class TaxPercentage:
    @staticmethod
    def tax_percentage(vehicle) -> float:
        if(vehicle.is_electric):
            return 0.02
        else:
            return 0.05


class Application:
    def register_vehicle(self, brand: string, catalogue_price: int, is_electric: bool):
        car = Vehicle(brand, catalogue_price, is_electric)
        print(f'Marca: {car.model}')
        print(f'ID: {car.id}')
        print(f'Placa: {car.license_plate}')
        print(f'Imposto a ser pago: {car.tax_percentage * car.catalogue_price}')

app = Application()
app.register_vehicle('Honda Civic LX',127900, True)

