--SQL File for Pet DB
--Initialize Pets table and insert values
--Created on 2/2/20
create table if not exists petTable
(
    petID integer PRIMARY KEY,
    petSpecies varchar(15),
    petSubSpecies varchar(20),
    petName varchar(15),
    petStatus varchar(15)
);
insert into petTable values (0, 'dog', 'Lab', 'Sparky', 'available');
insert into petTable values(1, 'dog', 'Husky', 'Spot', 'available');
insert into petTable values (2, 'dog', 'schnauzer', 'Pippin', 'available');
insert into petTable values (3, 'dog', 'Bulldog', 'Brutus', 'pending');
insert into petTable values (4, 'dog', 'Mutt', 'Sparky', 'sold');
insert into petTable values(5, 'cat', 'Persian', 'Princess', 'available');
insert into petTable values(6, 'cat', 'Sphinx', 'Pharaoh', 'pending');
insert into petTable values(7, 'cat', 'British Shorthair', 'Limmy', 'pending');
insert into petTable values(8, 'cat', 'American Shorthair', 'Ferguson', 'sold');
insert into petTable values(9, 'lizard', 'Chameleon', 'Camo', 'pending');
insert into petTable values(10, 'lizard', 'Gecko', 'geek', 'sold');