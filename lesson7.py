# база данных-хранилище
# СУБД-система управления базами данных
# SQLite3 mySQL posgreSQL
# sql - ЯЗЫК структурированных запросов
# CRUD-create reed update delete

import sqlite3
db=sqlite3.connect('user.db')
c=db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user(
name TEXT,
age INTEGER,
hobby TEXT
) ''')

# create - INSERT INTO
# c.execute(''' INSERT INTO user VALUES ('бека',42,'написал книгу о программе')''')


# delete - DELETE FROM WHERE
c.execute('''DELETE FROM user WHERE name="beka"''')

# update - UPDATE SET
c.execute(''' UPDATE user SET age=18 WHERE name="beka" ''')


# reed - SELSECT FROM
c.execute('''SELECT rowid,* FROM user WHERE rowid>0''')

for i in c.fetchall():
    print(i)

db.commit()
db.close()
