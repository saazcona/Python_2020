class Curso: #pascalcasing
    def __init__(self, titulo, cupos):
        self.titulo = titulo
        self.participantes = 0
        self.cupos = cupos
    
    def agregarParticipantes(self):
        if self.participantes < self.cupos:
            self.participantes += 1
        else:
            print("Ta to' lleno manin")

    def display(self):
        print(f"{self.titulo} cupos: {self.cupos} participantes inscritos: {self.participantes} Quedan {self.cupos - self.participantes}")


cursoSQL = Curso("Gestión de bases de datos SQL", 20)
cursoPython = Curso("POO Python", 30)

cursoSQL.display()
cursoSQL.agregarParticipantes()

cursoSQL.display()

cursoSQL.cupos = 15
cursoSQL.display()


# print(type(cursoSQL)) # Resultado es: <class '__main__.Curso'>

# #Este resultado me indica que la variable cursoSQL es del tipo creado como Curso

class Corolla:
    def __init__(self, galones, color):
        self.marca = "Toyota"
        self.cantidad_ruedas = 4
        self.cantidad_puertas = 4
        self.tipo_combustible = "gasolina"
        self.galones_combustible = galones
        self.color = color
        self.encendido = False

    def encender(self):
        if self.encendido == False and self.galones_combustible > 0:
            self.encendido = True
            print("El Corolla ta prendio")

    def apagar(self):
        if self.encendido:
            self.encendido = False


    def acelerar(self):
        if self.encendido:
            self.galones_combustible -= 1


    def frenar(self):
        print("Al auto se le paró")


# Instanciando objetos
corollaRojo = Corolla(5, "rojo")
corollaRojo = Corolla(9, "azul")

print(corollaRojo.galones_combustible)

### Herencias
# Se crea la clase Carro para utilizarla posteriormente

class Carro:
    def __init__(self):
        self.marca = "Toyota"
        self.cantidad_ruedas = None
        self.cantidad_puertas = None
        self.tipo_combustible = None
        self.galones_combustible = None
        self.color = None
        self.encendido = False

        def encender(self):
            pass

        def apagar(self):
            pass


        def acelerar(self):
            pass

        def frenar(self):
            print("Al auto se le paró")


# Se crea la clase Corolla en base a la clase Carro creada como plantilla
class Honda(Carro):
    pass

# # Ejemplo

class Persona:
    def __init__(self):
        self.nombre = ""
        self.nombre = ""
        self.cedula = ""
        self.telefono = ""

class Cliente(Persona):
    pass

class Empleado(Persona):
    def cobrar(self):
        pass

    def pasarInventario(self):
        pass

class Suplidor(Persona):
    pass

empleado1 = Empleado()
empleado1.cobrar()
