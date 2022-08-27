productos= input("Introduce los productos seleccionados separados por una ',': ")

p= productos.split(',')

for producto in p:
    print(producto.strip())