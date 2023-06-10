# Para poder usar esto tenéis que instalar estas librerías:
# pip3 install pdfkit
# pip3 install wkhtmltopdf
# si trabajáis con anaconda, creo que ya están todas instaladas
import pdfkit
import os

# listaProductos= [["Bebida Energética",2, 2.3],
#                  ["Bebida Diurética",1, 4.3]]
def addLineasProductos(listaProductos, listaCompra, listaUsuario):
    #le quito la tupla a las listas que vienen con ellas
    listaCompra  = [elemento for tupla in listaCompra  for elemento in tupla] 
    listaUsuario = [elemento for tupla in listaUsuario for elemento in tupla]
    # print(listaCompra)
    # print(listaUsuario)
    with open("facturaGenerada.html", "w") as f:
        #escribe cabecera
        f.write('''
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Factura</title>
    <!--Link CSS-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="https://carolmondesign.com/pdf_plantilla/css/estilo.css">
    <!-- Fuente de Google -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;600&display=swap" rel="stylesheet">
    
</head>
<body>
    <div id="todo" class="container-fluid">
        <table id="cabecera" class="d-flex flex-wrap align-items-center borderless-total">
            <td id="logo" class="col-3 borderless-total">
                <img class="img-thumbnail img-fluid" src="https://carolmondesign.com/pdf_plantilla/img/logo.png" alt="">
            </td>
            <td id="datosEmpresa" class="borderless-total">
                <p>Orgánic S.L</p>
                <p>C/General Ricardos, 177</p>
                <p>28025 Madrid</p>
                <p>B-53241998</p>
                <p>914 62 86 00</p>
                <p>ayuda@organic.com</p>
            </td>
        </table>
        <div id="datosPersona" class="mt-5 p-3">
            <p><strong>Nombre:</strong> '''+listaUsuario[0]+' '+listaUsuario[1]+'''</p>
            <p><strong>DNI:</strong> '''+listaUsuario[2]+'''</p>
            <p><strong>Dirección:</strong> '''+listaUsuario[3]+'''</p>
            <p><strong>Provincia:</strong> '''+listaUsuario[4]+'''</p>
            <p><strong>Código Postal:</strong> '''+str(listaUsuario[5])+'''</p>
        </div>
        <div class="mt-5"></div>
        <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Producto</th>
                <th scope="col">Cantidad</th>
                <th scope="col">Precio Unidad</th>
                <th scope="col">Precio Total</th>
              </tr>
            </thead>
            <tbody>
                    ''')
        
        #escribe los productos
        for x in range(len(listaProductos)):
            f.write('''
                <tr>
                    <th scope="row">'''+str(x+1)+'''</th>
                    <td>'''+listaProductos[x][0]+'''</td>
                    <td>'''+str(listaProductos[x][1])+'''</td>
                    <td>'''+str(listaProductos[x][2])+'''</td>
                    <td>'''+str(f"{listaProductos[x][1]*listaProductos[x][2]:.2f}")+'''</td>
                    
                </tr>''')
        
        total=listaCompra[1]
        precioSinIva=total/1.21
        iva=total-precioSinIva
        if listaCompra[2] == None:    
            descuento=0
        else:
            descuento=(total*(listaCompra[2]/100+1))-total
        f.write('''
                <tr>
                    <th scope="row" class="borderless-ultima"></th>
                    <td class="borderless-ultima"> </td>
                    <td class="borderless-ultima"> </td>
                    <td>Descuentos aplicados</td>
                    <td>'''+"-"+str(descuento)+'''</td>
                </tr>
                <tr>
                    <th scope="row" class="borderless"></th>
                    <td class="borderless"></td>
                    <td class="borderless"></td>
                    <td>PRECIO SIN IVA</td>
                    <td>'''+str(f"{precioSinIva:.2f}")+'''</td>
                </tr>
                <tr>
                    <th scope="row" class="borderless"></th>
                    <td class="borderless"></td>
                    <td class="borderless"></td>
                    <td>IVA</td>
                    <td>'''+str(f"{iva:.2f}")+'''</td>
                </tr>
                <tr>
                    <th scope="row" class="borderless"></th>
                    <td class="borderless"></td>
                    <td class="borderless"></td>
                    <td>PRECIO TOTAL</td>
                    <td>'''+str(f"{total:.2f}")+'''</td>
                </tr>         
                ''')            
        #escribe el final
        f.write("</tbody>")
        f.write("</table>")
        f.write("</div>")
        f.write("</body>")
        f.write("</html>")    
def rutaPdf(idCompra,fecha):
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/facturas_exportadas/factura_"+str(idCompra)+"_"+str(fecha)+".pdf"
    return ruta_salida

def rutaHtml():
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/facturaGenerada.html"
    return ruta_salida

def crea_pdf(idCompra,fecha,html):
    with open(html,"r") as archivo_html:
        contenido_html=archivo_html.read()
    config=pdfkit.configuration()
    pdfkit.from_string(contenido_html,rutaPdf(idCompra,fecha), configuration=config)