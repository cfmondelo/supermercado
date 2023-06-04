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

create table public.usuarios (
	correo 		varchar(50) 	unique not null,
	nombre	 	varchar(50) 	not null,
	contrasena 	varchar(100) 	not null,
	preg_seg 	varchar(50) 	not null,
	resp_seg	varchar(100) 	not null,
	direccion 	varchar(100) 	null,
	cp 			int 			null,
	ciudad 		varchar(50) 	null,
	municipio 	varchar(50) 	null,
    primary key (correo)
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
    precio 		int 		not null,
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
    precio 		int 		not null,
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
    precio 		int 		not null,
    cantidad 	int 		not null,
	primary key (usuario, prod_id),
    foreign key (prod_id)
    	references producto (prod_id)
);

