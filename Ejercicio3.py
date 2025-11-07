
class Carro: 
    marca = ""; 
    modelo = ""; 
    def __init__(self, marca, modelo):
        self.marca = marca; 
        self.modelo = modelo; 

    def mostrar_informacion(self): 
        print(f"La marca del carro es {self.marca} y el modelo es {self.modelo}")

#objeto1
carro1 = Carro("Toyota", 2006)
carro1.mostrar_informacion(); 

#objeto2
carro2 = Carro("Mazda", 2017)
carro2.mostrar_informacion()