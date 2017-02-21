#!/usr/bin/python
import psycopg2
from connectConfig import config

def create_tables():
	""" Create tables in the database """
	commands = (
	"""
	CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	user_name VARCHAR(255) NOT NULL
	)
	""",
	"""
	CREATE TABLE payments(
	user_id INTEGER NOT NULL,
	pay_id SERIAL PRIMARY KEY,
	pay_name VARCHAR(255) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id) 
	ON UPDATE CASCADE ON DELETE CASCADE
	)
	""")

	conn = None
	try:
		# read connection parameters
		params = config()
		
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# create table one by one
		for command in commands:
			cur.execute(command)
			
		# close the communication with the PostgreSQL
		cur.close()
		
		# commit the changes
		conn.commit()
		
		
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

if __name__=='__main__':
	create_tables()