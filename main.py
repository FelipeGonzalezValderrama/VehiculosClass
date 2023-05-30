from vehiculosClass import Automovil



num_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
vehiculos = []

for i in range(num_vehiculos):
    print("Datos del automóvil", i + 1)
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    numRuedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))

    automovil = Automovil(marca, modelo, numRuedas, velocidad, cilindrada)
    vehiculos.append(automovil)

print("Imprimiendo por pantalla los Vehículos:")
for i, automovil in enumerate(vehiculos):
    print("Datos del automóvil", i + 1, ":", "Marca", automovil.marca + ",", "Modelo", automovil.modelo + ",", automovil.numRuedas, "ruedas,", automovil.velocidad, "Km/h,")
    print(automovil.cilindrada, "cc")