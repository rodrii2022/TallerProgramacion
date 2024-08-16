class Persona:
    def __init__(self,name="",age=0,dni=0):
        self.name=name
        self.age=age
        self.dni=dni
    
    def mostrarDatos(self):
        print(f"Nombre: {self.name} \n"
              f"Edad: {self.age}\n"
              f"Dni: {self.dni}")
        
    def esMayor(self):
        return self.age >= 18
        
