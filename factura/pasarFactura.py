# Para poder usar esto tenéis que instalar estas librerías:
# pip3 install jinja2
# pip3 install pdfkit
# pip3 install wkhtmltopdf
# si trabajáis con anaconda, creo que ya están todas instaladas
import jinja2
import pdfkit

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
    ruta_salida="/Users/carolinaf.mondelo/Documents/GitHub/supermercado/factura/exportadas/factura.pdf"
    pdfkit.from_string(html,ruta_salida, configuration=config)
    
if __name__=="__main__":
    ruta_template='/Users/carolinaf.mondelo/Documents/GitHub/supermercado/factura/plantilla-factura.html'
    info={
        "NombreCliente"    : "Carolina Fernández",
        "DniCliente"       : "12345678L",
        "DireccionCliente" : "C/Maravillas, 123, 2ºA",
        "ProvinciaCliente" :"MADRID"
    }
    crea_pdf(ruta_template,info)