# Para poder usar esto tenéis que instalar estas librerías:
# pip3 install jinja2
# pip3 install pdfkit
# pip3 install wkhtmltopdf
# si trabajáis con anaconda, creo que ya están todas instaladas
import jinja2
import pdfkit
import os

listaProductos= [["Bebida Energética",2, 2.3],
                 ["Bebida Diurética",1, 4.3]]
def addLineasProductos(listaProductos, descuento=0):
    total=0
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
            <p><strong>Nombre:</strong> {{NombreCliente}}</p>
            <p><strong>DNI:</strong> {{DniCliente}}</p>
            <p><strong>Dirección:</strong> {{DireccionCliente}}</p>
            <p><strong>Municipio:</strong> {{ProvinciaCliente}}</p>
            <p><strong>Provincia:</strong> {{ProvinciaCliente}}</p>
            <p><strong>Código Postal:</strong> {{ProvinciaCliente}}</p>
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
            total+=(listaProductos[x][1]*listaProductos[x][2])
            f.write('''
                <tr>
                    <th scope="row">'''+str(x+1)+'''</th>
                    <td>'''+listaProductos[x][0]+'''</td>
                    <td>'''+str(listaProductos[x][1])+'''</td>
                    <td>'''+str(listaProductos[x][2])+'''</td>
                    <td>'''+str(f"{listaProductos[x][1]*listaProductos[x][2]:.2f}")+'''</td>
                    
                </tr>''')
        #escribe descuentos
        total-=descuento
        precioSinIva=total-(total*0.21)
        iva=total-precioSinIva
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
def rutaPdf():
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/exportadas/factura.pdf"
    return ruta_salida

def rutaHtml():
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/facturaGenerada.html"
    return ruta_salida

def crea_pdf(ruta_plantilla,info,rutacss=''):
    nombre_plantilla = ruta_plantilla.split('/')[-1] #obtiene el nombre de la plantilla sin la ruta completa
    ruta_plantilla   = ruta_plantilla.replace(nombre_plantilla,'') #obtiene la ruta sin el archivo
    # print(nombre_plantilla)
    # print(ruta_plantilla)
    env=jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_plantilla))
    plantilla=env.get_template(nombre_plantilla)
    html=plantilla.render(info)
    opcionesExportado={
        'page-size': 'A4',
        'encoding' : 'UTF-8'
    }
    config=pdfkit.configuration()
    pdfkit.from_string(html,rutaPdf(), configuration=config)
    
    
if __name__=="__main__":
    info={
        "NombreCliente"    : "Carolina Fernández",
        "DniCliente"       : "12345678L",
        "DireccionCliente" : "C/Maravillas, 123, 2ºA",
        "ProvinciaCliente" : "MADRID"
    }
    addLineasProductos(listaProductos) 
    crea_pdf(rutaHtml(),info)