# Para poder usar esto tenéis que instalar estas librerías:
# pip3 install jinja2
# pip3 install pdfkit
# pip3 install wkhtmltopdf
# si trabajáis con anaconda, creo que ya están todas instaladas
import jinja2
import pdfkit
import os
def addLineasProductos(numeroProd):
    with open("factura.html", "a") as f:
        f.write("<p>prueba</p>")
        f.write("</body>")
        f.write("</html>")
        
def rutaPdf():
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/exportadas/factura.pdf"
    return ruta_salida

def rutaHtml():
    ruta_absoluta=os.getcwd()
    ruta_salida=ruta_absoluta+"/factura.html"
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
    crea_pdf(rutaHtml(),info)