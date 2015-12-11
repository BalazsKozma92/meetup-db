
INSERT INTO meetups_db.Statuses (`id`, `value`) VALUES
	(1,'Going'),
	(2,'Tentative'),
	(3,'Not going'),
	(4,'Presenting');


INSERT INTO meetups_db.Users (`name`, `birthdate`, `introduction`, `avatar`, `email`) VALUES
	('Kozma Balazs', '1992-05-12', 'balazsvagyok', 'hmhmhmh', 'bal.kobr.1@gmail.com'),
	('Kozma Péter', '1998-05-21', 'petervagyok', '', 'gadhgdlg@gmail.com')


INSERT INTO meetups_db.Meetups (`start`, `location`, `topic`, `description`) VALUES
	('2015-12-06', 'Miskolc', 'donation', 'donateolni kell'),
	('2016-04-15', 'Miskolc', 'doneson', 'donateolni muszaj')