

fecha = input("Introduce una fecha en formato día/mes/año: ")
dia = fecha[:fecha.find("/")]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Día", dia)
print("Mes", mes)
print("Año", año)
