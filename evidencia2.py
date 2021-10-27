from collections import namedtuple
import csv 

SEPARADOR = "*" * 80
Registros = {}
Detalle = namedtuple("Detalle", "descripcion cantidad precio")
Clave_venta = namedtuple("Clave_venta", "folio fecha")

try:
    with open("Registros.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)
        lista_claves = []
        lista_registros = []
        for folio, fecha, descripcion, cantidad, precio in lector:
            clave = (Clave_venta(int(folio), fecha))
            if clave not in lista_claves:
                lista_claves.append(clave)
            lista_registros.append((Clave_venta(int(folio), fecha), Detalle(descripcion, int(cantidad), float(precio))))

        for clave in lista_claves:
            articulos = []
            for articulo in lista_registros:
                if clave == articulo[0]:
                    articulos.append(articulo[1])
            Registros[clave] = articulos

except Exception:
    print("No se encontro ningun archivo de respaldo")
    input("Presiona ENTER para continuar")

else: 
    print("Se encontro el archivo de respaldo")
    input("Presiona ENTER para continuar")


while True:
    print(SEPARADOR)
    print("Menú principal")
    print("1. Registrar una venta.")
    print("2. Consultar una venta.")
    print("3. Obtener un reporte de ventas para una fecha específica.")
    print("4. Salir")
    
    print(SEPARADOR)
    respuesta = int(input("Escribe el número con la opción deseada:"))
    print(SEPARADOR)
    
    if respuesta == 1:
        folio = int(input("Ingrese el folio de la venta: "))
        fecha = input("Ingresa la fecha de la venta (DD/MM/YYYY): ")
        clave_venta = Clave_venta(folio, fecha)
        ticket = []
        while True:
            descripcion = input("Descipcion del articulo: ")
            cantidad = int(input("Cantidad de piezas vendidas: "))
            precio = float(input("Precio del articulo: "))
            
            articulo_en_turno = Detalle(descripcion, cantidad, precio)
            ticket.append(articulo_en_turno)

            seguir_registrando = int(input("¿Seguir registrando articulos? Si=1, No=2: "))
            if seguir_registrando == 1:
                continue
            elif seguir_registrando == 2:
                total_venta = 0
                Registros[clave_venta] = ticket
                for articulo in Registros[clave_venta]:
                    total_articulo = articulo.cantidad * articulo.precio
                    total_venta = total_venta + total_articulo
                IVA = total_venta * .16
                total_mas_iva = total_venta + IVA
                print(f"El total de la venta es: {total_mas_iva}")
                print(f"El IVA de esta compra es de: {IVA}")
                input("Presiona ENTER para continuar")

                
                break

    elif respuesta == 2:
        folio_a_cosultar = int(input("Ingresa el folio de la venta a consultar: "))
        lista_claves = list(Registros.keys())
        for clave in lista_claves:
            if folio_a_cosultar == clave.folio:
                total = 0
                print(f"El folio de la venta es: {clave.folio}")
                print(f"La fecha de la venta es: {clave.fecha}")
                print(f'{"Cantidad de piezas":<15} | {"Descripcion":<15} | {"Precio venta":<15} | {"Total":<15} \n')
                for venta in Registros[clave]:
                    print(f"{venta.cantidad:<18} | {venta.descripcion:<15} | ${venta.precio:<15} | ${(venta.cantidad) * (venta.precio):<15}")
                    total_por_articulo = venta.cantidad * venta.precio
                    total = total + total_por_articulo
                iva = total * .16
                total_mas_iva = total + iva
                print(f"IVA (16%): {iva}")
                print(f'Total de la venta: {total_mas_iva}')
                input("Presiona ENTER para continuar")

    elif respuesta == 3:
        fecha_a_buscar = input("Ingresa la fecha de las ventas que deseas consultar(DD/MM/YYYY): ")
        lista_claves = list(Registros.keys())
        for clave in lista_claves:
            if fecha_a_buscar == clave.fecha:
                total = 0
                print(f"El folio de la venta es: {clave.folio}")
                print(f"La fecha de la venta es: {clave.fecha}")
                print(f'{"Cantidad de piezas":<15} | {"Descripcion":<15} | {"Precio venta":<15} | {"Total":<15}\n')
                for venta in Registros[clave]:
                    print(f"{venta.cantidad:<18} | {venta.descripcion:<15} | ${venta.precio:<15} | ${(venta.cantidad) * (venta.precio):<15}")
                    total_por_articulo = venta.cantidad * venta.precio
                    total = total + total_por_articulo
                iva = total * .16
                total_mas_iva = total + iva
                print(f"IVA (16%): {iva}")
                print(f'Total de la venta: {total_mas_iva}')
        input("Presiona ENTER para continuar")

    elif respuesta == 4:
        confirmacion = int(input("¿Esta seguro de que desea salir? (1=Si, 2=No)"))
        if confirmacion == 1:
            with open("Registros.csv", "w", newline="") as archivo:
                        grabador = csv.writer(archivo)
                        for clave, detalle in Registros.items():
                            for articulo in detalle:
                                grabador.writerow((clave.folio, clave.fecha, articulo.descripcion, articulo.cantidad, articulo.precio))
            break
        elif confirmacion == 2:
            continue