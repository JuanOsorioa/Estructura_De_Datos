class MotorElectrico:
    potencia = None
    def encender(self):
        print("Encendiendo el motor electrico")

    def __init__(self):
        pass

objeto = MotorElectrico()
objeto.potencia = 1000
objeto.encender()
print("Primer codigo en python")
