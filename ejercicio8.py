precio = input("introduce el precio del producto con dos decimales: ")
print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "centimos.")
