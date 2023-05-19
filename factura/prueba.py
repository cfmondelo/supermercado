def addLineasProductos():
    with open("factura.html", "a") as f:
        f.write("<p>prueba</p>")
        f.write("</body>")
        f.write("</html>")
        
listaProductos= [["Bebida Energética",2, 2.3, 4.6],
                 ["Bebida Diurética",1, 4.3, 4.3]]
print(len(listaProductos))
factura='''
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
        <div id="cabecera" class="row d-flex flex-wrap align-items-center">
            <div id="logo" class="col-2">
                <img class="img-thumbnail img-fluid" src="https://carolmondesign.com/pdf_plantilla/img/logo.png" alt="">
            </div>
            <div id="datosEmpresa" class="col-6">
                <p>Orgánic S.L</p>
                <p>C/General Ricardos, 177</p>
                <p>28025 Madrid</p>
                <p>B-53241998</p>
                <p>914 62 86 00</p>
                <p>ayuda@organic.com</p>
            </div>
        </div>
        <div id="datosPersona" class="mt-5 p-5">
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
            <tbody>'''