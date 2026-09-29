
# SQL databse setup

You can use AI to help you populate your app database with data.  Here is an example.

It can create both the SQL and the data.  You might want to use your own data so in that case collate the data in Excel and pass the file, as a CSV file, to the AI.


## Makers table

*AI Prompt*
Give me 6 SQL INSERT statement, like the following one, and populate the values with the correct information for bike makers, such as Yamaha, Suzuki, Honda and KTM.
e.g.
INSERT INTO Makers (MakerID, Name) VALUES (1, "KTM");

*Result* 
INSERT INTO Makers (MakerID, Name) VALUES (1, 'Yamaha');
INSERT INTO Makers (MakerID, Name) VALUES (2, 'Suzuki');
INSERT INTO Makers (MakerID, Name) VALUES (3, 'Honda');
INSERT INTO Makers (MakerID, Name) VALUES (4, 'KTM');
INSERT INTO Makers (MakerID, Name) VALUES (5, 'Kawasaki');
INSERT INTO Makers (MakerID, Name) VALUES (6, 'Ducati');

## Bikes table

*AI Prompt*
Give me 12 SQL INSERT statement, like the following one, and populate the values with the correct information for at least one bike from each of the makers.  e.g. Yamaha, Suzuki and Honda.  
Put the statements one after another in a code box.
e.g.
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description)
VALUES (1, 1, "R1", 250, 20000, "A great all rounder");


*Result* 
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (1, 1, 'YZF-R1', 299, 19999, 'A high-performance superbike built for the track');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (2, 1, 'MT-09', 220, 11999, 'A naked roadster with an aggressive triple-cylinder engine');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (3, 2, 'GSX-R1000', 299, 17999, 'A legendary sportbike with razor-sharp handling');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (4, 2, 'V-Strom 650', 209, 9499, 'A versatile adventure tourer great for long-distance rides');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (5, 3, 'CBR1000RR-R', 299, 28999, 'Hondas flagship superbike with MotoGP-inspired technology');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (6, 3, 'Africa Twin', 217, 15999, 'A rugged adventure bike built for on and off-road exploration');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (7, 4, '1290 Super Duke R', 290, 22999, 'A ferocious naked bike known as The Beast');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (8, 4, '390 Duke', 167, 5999, 'A lightweight and nimble entry-level street fighter');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (9, 5, 'Ninja ZX-10R', 299, 18499, 'A championship-winning superbike with elite track performance');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (10, 5, 'Z900', 240, 10499, 'A punchy naked bike with a bold aggressive style');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (11, 6, 'Panigale V4', 305, 28995, 'An Italian masterpiece combining breathtaking power and beauty');
INSERT INTO Bikes (BikeID, MakerID, Model, TopSpeed, Cost, Description) VALUES (12, 6, 'Monster 937', 225, 13995, 'A iconic naked bike with a characterful V-twin engine');


