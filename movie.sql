create table actor ( act_id int (3),act_name varchar (20),act_gender char (1),primary key (act_id));

create table director (dir_id int (3),dir_name varchar (20),dir_phone int (10),primary key (dir_id));

create table movies (mov_id int (4),mov_title varchar (25),mov_year int (4),mov_lang varchar (12),dir_id int (3),primary key (mov_id),foreign key (dir_id) references director (dir_id));

create table movie_cast (act_id int (3),mov_id int (4),role varchar (10),primary key (act_id, mov_id),foreign key (act_id) references actor (act_id),foreign key (mov_id) references movies (mov_id));

create table rating (mov_id int (4),rev_stars varchar (25),primary key (mov_id),foreign key (mov_id) references movies (mov_id));
