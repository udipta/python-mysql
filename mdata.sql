insert into actor values (301,'anushka','f');
insert into actor values (302,'prabhas','m');
insert into actor values (303,'nana pathekar','m');
insert into actor values (304,'jermy','m');
insert into actor values (305,'heath ledger','m');

insert into director values (60,'rajamouli', 87516110);
insert into director values (61,'hitchcock', 77661389);
insert into director values (62,'ram gopal varma', 99867765);
insert into director values (63,'steven spielberg', 89897530);
insert into director values (64,'christopher nolan', 75897530);

insert into movies values (1001,'bahubali-2', 2017, 'telagu', 60);
insert into movies values (1002,'bahubali-1', 2015, 'telagu', 60);
insert into movies values (1003,'the attack of 26/11', 2013, 'hindi', 62);
insert into movies values (1004,'war horse', 2011, 'english', 63);
insert into movies values (1005,'the dark knight', 2012, 'english', 64);

insert into movie_cast values (301, 1002, 'heroine');
insert into movie_cast values (301, 1001, 'heroine');
insert into movie_cast values (303, 1003, 'hero');
insert into movie_cast values (304, 1002, 'guest');
insert into movie_cast values (305, 1005, 'villain');

insert into rating values (1001, 4);
insert into rating values (1002, 2);
insert into rating values (1003, 5);
insert into rating values (1004, 4);
insert into rating values (1005, 5);
