import sqlite3
conn=sqlite3.connect('users.db')
conn.executescript('''drop table if exists user_info;
create table user_info(
    id integer primary key autoincrement,
    user_id text not null,
    user_pass text not null
);
drop table if exists todo;
create table todo(
    id integer not null,
    task_heading text not null,
    task_desc text not null,
    task_date text not null,
    img text
);
insert into user_info values(1001,'admin@gmail.com','admin');
''')
conn.commit()
cur=conn.cursor()
cur.execute('select * from todo;')
rows = cur.fetchall()
print(rows)
conn.close()
