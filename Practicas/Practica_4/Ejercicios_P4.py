# ~~~~~~~~~~~~~~~~~~~~~~~~
# Práctica 4: Saul Azcona
# ~~~~~~~~~~~~~~~~~~~~~~~~

# 1- Modele tres entidades del mundo real, colocar por lo menos 3
# características distintivas.

# Entidad 1: Poste de luz

class Poste:
    def __init__(self, estructura, altura, capacidad):
        self.estructura = estructura
        self.altura = altura
        self.capacidad = capacidad

    def info_poste(self):
        print(f"Estructura: {self.estructura} | Altura: {self.altura} m | Capacidad: {self.capacidad} daN")


poste_concreto = Poste("Hormigón Pretensado", 12, 500)
poste_metal = Poste("Metálico de chapas", 9, 300)

poste_concreto.info_poste()
poste_metal.info_poste()

# Entidad 2: Lámparas
class Lampara:
    def __init__(self, tipo, potencia, voltaje, color_luz):
        self.tipo = tipo
        self.potencia = potencia
        self.voltaje = voltaje
        self.color_luz = color_luz
        self.corriente = round(float(potencia / voltaje), 2)

    def mostrar_datos(self):
        print(f"Tipo: {self.tipo} | Potencia: {self.potencia}W | Voltaje: {self.voltaje}V | Corriente: {self.corriente}A Color: {self.color_luz}")


lampara_led = Lampara("Led", 7, 120, "Blanco")
lampara_led.mostrar_datos()

lampara_fluorescente = Lampara("Fluorescente", 15, 120, "Blanca")
lampara_fluorescente.mostrar_datos()

# Entidad 3
class Cefalopodos:
    def __init__(self, orden, extremidades, veneno, camuflaje):
        self.orden = orden
        self.cantidad_entremidades = extremidades
        self.esVenenoso = veneno
        self.camuflaje = camuflaje

    def datos(self):
        print(f"Orden: {self.orden} | Cantidad de extremidades: {self.cantidad_entremidades} | Peligro humano: {self.esVenenoso} | Capacidad de camuflajearse: {self.camuflaje}")


pulpo = Cefalopodos("Octópodo", 8, True, True)
pulpo.datos()

calamar = Cefalopodos("Téutido", 10, False, True)
calamar.datos()

nautilus = Cefalopodos("Nautilino", 90, False, False)
nautilus.datos()

# ---------------------------------------------------------------------------------------
# 2- Crear una clase llamada Estudiante con un campo llamado promedio, el cual
# solo podrá ser accedido mediante un metodo. El valor del promedio no puede
# estar por encima de 100 que es la nota máxima.

class Estudiante:
    def __init__(self, matricula, nombre, materia, promedio):
        self.matricula = matricula
        self.nombre = nombre
        self.asignatura = materia
        self.nota_promedio = promedio

    def promedio_estudiante(self):
        if self.nota_promedio > 100:
            print(f"El estudiante {self.nombre} tiene una nota por encima de 100")
        else:
            print(f"Matricula: {self.matricula} | Estudiante: {self.nombre} | Asignatura: {self.asignatura} | Promedio: {self.nota_promedio}")
        

Jonas = Estudiante('1234-5678', 'Jonas', 'Matematicas', 95)
Edward = Estudiante('1234-9101', 'Edward', 'Alquimia', 110)
Zoro = Estudiante('1234-1112', 'Bob', 'Geografía', 50)


Jonas.promedio_estudiante()
Edward.promedio_estudiante()
Zoro.promedio_estudiante()

# ---------------------------------------------------------------------------------------
# 3- Hacer una clase llamada Aritmética, que contenga métodos para cada una de
# las operaciones aritméticas básicas.

class Aritmetica:
    def __init__(self, operacion):
        self.tipo_operacion = operacion

    def Suma(self, num1, num2):
        if self.tipo_operacion == "Suma":
            resultado = num1 + num2
            return print("Resultado: " + str(resultado))
        else:
            print("Operación aritmética no reconocida")

    def Resta(self, num1, num2):
        if self.tipo_operacion == "Resta":
            resultado = num1 - num2
            return print("Resultado: " + str(resultado))
        else:
            print("Operación aritmética no reconocida")

    def Multiplicacion(self, num1, num2):
        if self.tipo_operacion == "Multiplicar":
            resultado = num1 * num2
            return print("Resultado: " + str(resultado))
        else:
            print("Operación aritmética no reconocida")

    def Division(self, num1, num2):
        if self.tipo_operacion == "Division":
            resultado = num1 / num2
            return print("Resultado: " + str(resultado))
        else:
            print("Operación aritmética no reconocida")

sumar_numeros = Aritmetica("Suma")
restar_numeros = Aritmetica("Resta")
multiplicar_numeros = Aritmetica("Multiplicar")
dividir_numeros = Aritmetica("Division")

no_existe = Aritmetica("Potenciacion") # ← ← ← ← ←

sumar_numeros.Suma(2, 2)
restar_numeros.Resta(1, 5)
multiplicar_numeros.Multiplicacion(5, 5)
dividir_numeros.Division(10, 2)

no_existe.Multiplicacion(10, 2) # ← ← ← ← ←

# ---------------------------------------------------------------------------------------
# 4- Cree una clase llamada Personaje con los métodos de instancia MoverArriba,
# MoverAbajo, MoverDerecha y MoverIzquierda. Cree una clase llamada Mario y
# otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.

class Personaje:
    def __init__(self):
        self.nombre_personaje = ""
    
    def MoverArriba(self):
        print(f"↑ ↑ ↑ ↑ {self.nombre_personaje} ↑ ↑ ↑ ↑")

    def MoverAbajo(self):
        print(f"↓ ↓ ↓ ↓ {self.nombre_personaje} ↓ ↓ ↓ ↓")

    def MoverDerecha(self):
        print(f"→ → → → {self.nombre_personaje} → → → →")

    def MoverIzquierda(self):
        print(f"← ← ← ← {self.nombre_personaje} ← ← ← ←")


class Mario(Personaje):
    def __init__(self):
        self.nombre_personaje = "Mario"

class Koopa(Personaje):
    def __init__(self):
        self.nombre_personaje = "Koopa"

m = Mario()
kp = Koopa()

m.MoverArriba()
m.MoverAbajo()
m.MoverDerecha()
m.MoverIzquierda()

kp.MoverArriba()
kp.MoverAbajo()
kp.MoverDerecha()
kp.MoverIzquierda()

# Vea esto por favor...: https://www.youtube.com/watch?v=ff9ldkz1h1M

# ---------------------------------------------------------------------------------------
# 5- Cree una clase Carro, con un campo llamado _cantidadCombustible y un
# método que se llame Encender el cual en base a la gasolina disponible
# mostrara si el carro pudo o no avanzar. Cada vez que el método se ejecute,
# deberá restarse 1 a la gasolina disponible. La cantidad de gasolina debe
# establecerse al momento de instanciar un objeto de del tipo de la clase.

class Carro:
    def __init__(self, marca, modelo, fuel_type, volumen_tanque, gal_disponible):
        self.marca_carro = marca
        self.modelo_carro = modelo
        self.cantidad_ruedas = 4
        self.cantidad_puertas = 4
        self.tipo_combustible = fuel_type
        self.tanque_combustible = volumen_tanque
        self.cantidad_combustible = gal_disponible
        self.encendido = False

    # Método para encerder el vehículo
    def encender(self):
        if self.encendido == False and self.cantidad_combustible > 0:
            self.encendido = True
            self.cantidad_combustible -= 1
            print("El vehículo está encendido")
        elif self.cantidad_combustible == 0:
            print("Tanque vacío, llenar el combustible por favor")
        else:
            print("El vehículo ya está encendido")

    # Método para acelerar el vehículo
    def acelerar(self):
        if self.encendido == True and self.cantidad_combustible > 0:
            print(f"Carro acelerando... Nivel Combustible: {self.cantidad_combustible}")
            self.cantidad_combustible -= 1
            # Si el carro está en un 30% de combustible
            if self.cantidad_combustible <= (self.tanque_combustible * 0.30):
                print(f"Vehículo en reserva, Nivel de Combustible: {self.cantidad_combustible} galones")
        else:
            print("Carro se ha quedado sin combustible y está apagado!!!")
            self.encendido = False

    # Método para llenar el combustible
    def llenar_combustible(self, refill):
        self.refill = refill
        if self.refill > self.tanque_combustible:
            print("Tanque lleno")
            self.refill = self.tanque_combustible
            self.cantidad_combustible = self.refill
        else:
            self.cantidad_combustible = self.refill
            print(f"Cantidad de galones echados: {self.refill}")
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Se ha apagado el vehículo")

# Instanciando un carro
toyota_corolla = Carro("Toyota", "Corolla", "Gasolina", 10, 10)

# Encendiendo el vehículo
toyota_corolla.encender()

# Acelerando el vehículo
toyota_corolla.acelerar() # Acelerón 1
toyota_corolla.acelerar() # Acelerón 2
toyota_corolla.acelerar() # Acelerón 3
toyota_corolla.acelerar() # Acelerón 4
toyota_corolla.acelerar() # Acelerón 5
toyota_corolla.acelerar() # Acelerón 6
toyota_corolla.acelerar() # Acelerón 7
toyota_corolla.acelerar() # Acelerón 8
toyota_corolla.acelerar() # Acelerón 9

# A partir de aquí el vehículo se ha apagado
toyota_corolla.acelerar() # Acelerón 10
toyota_corolla.acelerar() # Acelerón 11

# Si se intenta encender nuevamente...
toyota_corolla.encender()

# Se necesita hechar combustible
toyota_corolla.llenar_combustible(10)