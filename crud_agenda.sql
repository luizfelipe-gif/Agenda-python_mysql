drop database crud_agenda;
create database crud_agenda;
use crud_agenda;

create table contatos(
	id int not null auto_increment primary key,
    nome varchar(150),
    email varchar(150),
    telefone varchar(11),
    tipoTelefone varchar(11)
);

select * from contatos;