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

vehicle1 = Vehicle("Mitsubishi", "Gas")

print(vehicle1)

