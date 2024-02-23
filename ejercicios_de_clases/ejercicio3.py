class Vehicle:
    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible

    def encender(self):
        print("El vehiculo está prendido")

    def arrancar(self):
        print("El vehiculo está arrancando")

    def __str__(self):
        return f"Vehiculo marca: {self.marca} ___ combustible: {self.combustible}"

class Moto(Vehicle):
    def __init__(self, marca, combustible, tiempos):
        super().__init__(marca, combustible)
        self.tiempos = tiempos
    def __str__(self):
        return f"Moto marca: {self.marca}, combustible: {self.combustible}, tiempos: {self.tiempos}"
    
class Car(Vehicle):
    def __init__(self, marca, combustible, modelo):
        super().__init__(marca, combustible)
        self.modelo = modelo

    def __str__(self):
        return f"Carro marca: {self.marca}, combustible: {self.combustible}, modelo: {self.modelo}"
    
moto1 = Moto("Yamaha", "Gasolina", "4T")
car1 = Car("Tesla", "Electricidad", "2022")

print(moto1)
print(car1)