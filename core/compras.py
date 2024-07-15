class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, camion):
        if camion.placa not in self.carrito.keys():
            self.carrito[camion.placa]={
                "placa":camion.placa, 
                "marca": camion.marca,
                "modelo": camion.modelo,
                "precio": str (camion.precio),
                "cantidad": 1,
                "total": camion.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==camion.placa:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = camion.precio
                    value["total"]= value["total"] + camion.precio
                    break
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, camion):
        id = camion.placa
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,camion):
        for key, value in self.carrito.items():
            if key == camion.placa:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- camion.precio
                if value["cantidad"] < 1:   
                    self.eliminar(camion)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
