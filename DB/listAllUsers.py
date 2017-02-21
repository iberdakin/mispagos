#!/usr/bin/python
import psycopg2
from connectConfig import config

def list_users():
	"""query data from users table"""
	
	conn = None
	try:
		# read connection parameters
		params = config()
		
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute("SELECT * FROM users ORDER BY user_id ASC")
		rows = cur.fetchall()
			
		# close the communication with the PostgreSQL
		cur.close()		
		
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')
		
	return	rows	