create table public.producto (
	prod_id 	serial  	not null,
	nombre 		varchar(50) unique not null,
	descripcion varchar(100) not null,
	categoria 	varchar 	not null,
	precio 		float4 		not null,
	cantidad 	int 		not null,
	imagen 		varchar(50) not null,
    primary key (prod_id)
);

CREATE TABLE CCAA (
    idCCAA int NOT NULL,
    Nombre varchar(100) NOT NULL,
    PRIMARY KEY (idCCAA)
) ;

CREATE TABLE PROVINCIAS (
    idProvincia int NOT NULL,
    idCCAA      int NOT NULL,
    Provincia   varchar(30) DEFAULT NULL,
    PRIMARY KEY (idProvincia)
);

CREATE TABLE MUNICIPIOS (
    idMunicipio   serial NOT NULL,
    idProvincia   int NOT NULL,
    codMunicipio  int NOT NULL,
    DC            int NOT NULL,
    Municipio     varchar(100) NOT NULL,
    PRIMARY KEY (idMunicipio)
);

create table public.usuarios (
	correo 		varchar(50) 	unique not null,
	nombre	 	varchar(50) 	not null,
	contrasena 	varchar(100) 	not null,
	preg_seg 	varchar(50) 	not null,
	resp_seg	varchar(100) 	not null,
	direccion 	varchar(100) 	null,
	cp 			int 			null,
	id_ca 		int 	null,
	id_provincia	int 	null,
	id_municipio 	int 	null,
	telefono	int			null,
	dni         varchar(9)      null,
	Apellidos   varchar(50)     null,
    primary key (correo),
    foreign key (id_ca)
    	references CCAA (idCCAA),
    foreign key (id_municipio)
    	references MUNICIPIOS (idMunicipio), 
    foreign key (id_provincia)
    	references PROVINCIAS (idProvincia)
    
);

create table public.descuentos (
	desc_id 	serial 		not null,
	código		varchar(15) not null,
	descuento 	int 		not null,
	activo 		boolean		not null,
	primary key (desc_id)
);

create table public.tickets (
    tick_id 	serial 		not null,
    usuario 	varchar(50) not null,
    desc_id		int 		null,
    precio 		float4		not null,
	fecha	 	date 		not null,
    primary key (tick_id),
    foreign key (usuario)
    	references usuarios (correo),
    foreign key (desc_id)
    	references descuentos (desc_id)
);

create table public.lineapedidos (
	linea_id	serial		not null,
    prod_id 	int 		not null,
    precio 		float4 		not null,
    cantidad 	int 		not null,
    compra_id	int			not null,
    primary key (linea_id),
    foreign key (prod_id)
    	references producto (prod_id),
    foreign key (compra_id)
    	references tickets (tick_id)
);

create table public.carrito (
	usuario 	varchar(50) not null,
    prod_id 	int 		not null,
    precio 		float4 		not null,
    cantidad 	int 		not null,
	primary key (usuario, prod_id),
    foreign key (prod_id)
    	references producto (prod_id)
);

