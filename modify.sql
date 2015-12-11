
UPDATE meetups_db.Meetups
	SET Topic='conference'
	WHERE Topic='party';

UPDATE meetups_db.Users
	SET Name='Peet Owl', Email='djpetyaaa@gmail.com'
	WHERE Name='Bagoly Péter';