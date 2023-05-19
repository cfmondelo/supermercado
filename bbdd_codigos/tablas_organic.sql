create table public.producto (
	prod_id 	serial  	not null,
	nombre 		varchar(50) unique not null,
	descripcion varchar(50) not null,
	categoria 	varchar 	not null,
	precio 		float4 		not null,
	cantidad 	int 		not null,
	imagen 		varchar(50) not null,
    primary key (prod_id)
);

create table public.usuarios (
	nombreusu 	varchar(50) not null,
	contrasena 	varchar(50) not null,
	correo 		varchar(50) not null,
	preg_seg 	varchar(50) not null,
	resp_seg	varchar(50) not null,
	direccion 	varchar(50) null,
    primary key (nombreusu)
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
    prod_id 	int 		not null,
    desc_id		int 		null,
    precio 		int 		not null,
    cantidad 	int 		not null,
	fecha	 	date 		not null,
    primary key (tick_id, usuario, prod_id),
    foreign key (usuario)
    	references usuarios (nombreusu),
    foreign key (prod_id)
    	references producto (prod_id),
    foreign key (desc_id)
    	references descuentos (desc_id)
);