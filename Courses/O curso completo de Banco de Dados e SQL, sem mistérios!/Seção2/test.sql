/* Modeling the DB*/


/*

CLIENT:
	NAME 	- CHAR(30)
	ID   	- NUM (11)
	EMAIL 	- CHAR(30)
	NUMBER 	- CHAR(30)
	ADRESS 	- CHAR(100)
	SEX 	- CHAR(1)
*/


CREATE DATABASE ex;
CREATE DATABASE PROJECT;

/* CONECT TO THE DATABASE */

USE PROJECT;

/* Creating the clients table */

CREATE TABLE CLIENTS
(
	NAMES VARCHAR(30), -- VARCHAR  - DYNAMIC ALLOCATION IN MEMORY
	ID INT(11),
	EMAIL VARCHAR(30),
	NUMBERS VARCHAR(30),
	ADRESS VARCHAR(100),
	SEX CHAR(1)        -- CHAR - MORE PERFOMATIC BUT WITH STATIC ALLOCATION IN MEMORY
); 


/* HOW TO KNOW THE STRUCTURE OF A TABLE */

DESC CLIENTS;


--INSERT INTO CLIENTS VALUES()