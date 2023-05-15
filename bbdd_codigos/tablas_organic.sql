create table public.producto (
	prod_id 	serial  	not null,
	nombre 		varchar(50) unique not null,
	precio 		float4 		not null,
	categoria 	varchar 	not null,
	fechacad 	date 		null,
	cantidad 	int 		not null,
	descripcion varchar(50) not null,
	imagen 		varchar(50) not null,
    primary key (prod_id)
);

create table public.usuarios (
	nombreusu 	varchar(50) not null,
	contrasena 	varchar(50) not null,
	correo 		varchar(50) not null,
	direccion 	varchar(50) null,
    primary key (nombreusu)
);

create table public.cupones (
	cup_id 		serial 	not null,
	prod_id 	int 	not null,
	descuento 	int 	not null,
	fechaini 	date 	not null,
	fechafin 	date 	not null,
	primary key (cup_id),
    foreign key (prod_id)
    	references producto (prod_id)
);

create table public.tickets (
    tick_id 	serial 		not null,
    usuario 	varchar(50) not null,
    prod_id 	int 		not null,
    cup_id 		int 		not null,
    precio 		int 		not null,
    cantidad 	int 		not null,
	fecha	 	date 		not null,
    primary key (tick_id, usuario, prod_id),
    foreign key (prod_id)
    	references producto (prod_id),
    foreign key (cup_id)
    	references cupones (cup_id)
);