class Cohete():
    def __init__(self, ID, capacidad, autonomia, fabricante):
        self.ID = ID
        self.capacidad = capacidad
        self.autonomia = autonomia
        self.fabricante = fabricante
        self.estado= "libre"
        self.combustible = 10000
        
    def mostrar(self):
        print("ID: ", self.ID)
        print("Capacidad: ", self.capacidad)
        print("Autonomia: ", self.autonomia)
        print("Fabricante: ", self.fabricante)
        print("Estado: ", self.estado)
        print("Combustible: ", self.combustible)
    def set_autonomia(self, rango):
        self.autonomia = rango
    def calcular_velocidad(km, horas):
        velocidad = km / horas
        return velocidad
    def factibilidad_viaje(self, distancia_a_destino):
        if self.autonomia >= distancia_a_destino:
            return "El viaje es factible"
        else:               
            return "El viaje no es factible"   
        if self.combustible >= self.autonomia/2:
            return "El viaje es factible"
        else:
            return "El viaje no es factible"
        def calcular_ganancias(self, cantidad_pasajeros, distancia_total_viaje):
            boleto = 10000
            costo= 100
            ganancias = (boleto * cantidad_pasajeros) - (costo * distancia_total_viaje)
            return ganancias
        if self.estado == "libre":
            return "El cohete está disponible para un nuevo viaje"
        else:
            def enviar_reparacion():
                self.estado = "en reparación"
                return "El cohete ha sido enviado a reparación"
        def finalizar_reparación(self):
            self.estado = "libre"
            return "El cohete ha sido reparado y está disponible"
Cohete_1 = Cohete("SV-01", 10, 10000, "Rocket Astra")
