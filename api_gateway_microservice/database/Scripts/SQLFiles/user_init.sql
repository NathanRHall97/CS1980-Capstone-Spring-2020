--SQL File for User DB
--Initialize User table and insert values
--Created on 2/2/20

CREATE TABLE IF NOT EXISTS users
(
    userID INTEGER PRIMARY KEY,
    userName varchar(15),
    userRole varchar(15)
);

insert into users values(0, 'Jerry James', 'Customer');
insert into users values(1, 'Kayla Riggs', 'Customer');
insert into users values(2, 'Nate Hall', 'Customer');
insert into users values(3, 'Merry Lou', 'Customer');