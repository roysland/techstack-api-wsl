import sqlite3

connection = sqlite3.connect('finnstack.sqlite')
connection.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
cursor = connection.cursor()