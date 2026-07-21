def descuento(precio, descuento):

    if descuento >= 51:
        print("El descuento no puede ser mayor a 50%")
        return precio

    elif descuento >= 50:
        print("Descuento del 50%")
    else:
        print("Descuento del", descuento, "%")

    return precio - (precio * descuento / 100)

precio_con_descuento = descuento(100, 60)
print(f"Precio final: {precio_con_descuento}")

