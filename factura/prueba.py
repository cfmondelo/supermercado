def addLineasProductos():
    with open("factura.html", "a") as f:
        f.write("<p>prueba</p>")
        f.write("</body>")
        f.write("</html>")
        
listaProductos= [["Bebida Energética",2, 2.3, 4.6],
                 ["Bebida Diurética",1, 4.3, 4.3]]
print(len(listaProductos))
