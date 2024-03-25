class Te:
    # Atributos de clase
    precios = {300: 3000, 500: 5000}
    tiempos = {1: 3, 2: 5, 3: 6}
    recomendaciones = {
        1: "Consumir al desayuno",
        2: "Consumir al medio día",
        3: "Consumir al atardecer"
    }
    
    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        tiempo = Te.tiempos.get(sabor)
        recomendacion = Te.recomendaciones.get(sabor)
        return tiempo, recomendacion
    
    @staticmethod
    def obtener_precio(formato):
        precio = Te.precios.get(formato)
        return precio
